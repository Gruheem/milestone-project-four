from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    category_name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True, blank=True)
    category_friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name
    
    def get_category_friendly_name(self):
        return self.category_friendly_name
    

class ProductType(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_type = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True, blank=True)
    product_type_friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'category',
                    'product_type'
                ],
                name='unique_category_product_type'
            )
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_type)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_type
    
    def get_product_type_friendly_name(self):
        return self.product_type_friendly_name
    

class Attribute(models.Model):
    class ValueType(models.TextChoices):
        TEXT = 'text', 'Text'  
        NUMBER = 'number', 'Number'  
        BOOLEAN = 'boolean', 'Boolean'

    product_type = models.ForeignKey('ProductType', on_delete=models.CASCADE)
    attribute = models.CharField(max_length=254)
    attribute_friendly_name = models.CharField(max_length=254)
    value_type = models.CharField(max_length=10, choices=ValueType.choices, default=ValueType.TEXT)    

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'product_type',
                    'attribute'
                ],
                name='unique_product_type_attribute'
            )
        ]

    def __str__(self):
        return self.attribute
    
    def get_attribute_friendly_name(self):
        return self.attribute_friendly_name
    

class AttributeValue(models.Model):
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=254, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'attribute',
                    'attribute_value'
                ],
                name='unique_attribute_value'
            )
        ]

    def __str__(self):
        return self.attribute_value
    

class Product(models.Model):
    product_type = models.ForeignKey('ProductType', on_delete=models.PROTECT)
    sku = models.CharField(max_length=254, null=True, blank=True)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    product_name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.CharField(max_length=254)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    imageURL = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

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