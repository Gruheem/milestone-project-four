from django.contrib import admin
from .models import Category, ProductType, Product, Attribute, AttributeValue, ProductAttributeValue
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category_name',
        'slug',
        'category_friendly_name',
    ]

class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'product_type',
        'slug',
        'product_type_friendly_name',
    ]
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_type',
        'sku',
        'stock',
        'available',
        'product_name',
        'slug',
        'description',
        'price',
        'brand',
        'rating',
        'imageURL',
        'image',
    ]

class AttributeAdmin(admin.ModelAdmin):
    list_display = [
        'product_type',
        'attribute', 
        'attribute_friendly_name',
        'value_type',
    ]

class AttributeValueAdmin(admin.ModelAdmin):
    list_display = [
        'attribute',
        'attribute_value',
    ]

class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'attribute',
        'attribute_value',
    ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(AttributeValue, AttributeValueAdmin)
admin.site.register(ProductAttributeValue, ProductAttributeValueAdmin)