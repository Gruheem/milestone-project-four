from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=254)
    category_friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.category
    
    def get_category_friendly_name(self):
        return self.category_friendly_name
    

class ProductType(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=254)
    product_type_friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.product_type
    
    def get_product_type_friendly_name(self):
        return self.friendly_name
    

class Attribute(models.Model):
    product_type = models.ForeignKey('ProductType', null=True, blank=True, on_delete=models.SET_NULL)
    attribute = models.CharField(max_length=254)
    attribute_friendly_name = models.CharField(max_length=254)

    class Meta:
        unique_together = ('product_type', 'attribute')

    def __str__(self):
        return self.attribute
    
    def get_attribute_friendly_name(self):
        return self.attribute_friendly_name
    

class AttributeValue(models.Model):
    class ValueType(models.TextChoices):
        TEXT = 'text', 'Text'  
        NUMBER = 'number', 'Number'  
        BOOLEAN = 'boolean', 'Boolean' 
    
    attribute = models.ForeignKey('Attribute', null=True, blank=True, on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=254, db_index=True)
    value_type = models.CharField(max_length=10, choices=ValueType.choices, default=ValueType.TEXT)    

    def __str__(self):
        return self.attribute_value
    

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL) 
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField
    price = models.DecimalField
    brand = models.CharField
    rating = models.DecimalField
    imageURL = models.URLField
    image = models.ImageField


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'product',
                    'attribute'
                ],
                name='unique_product_attribute'
            )
        ]