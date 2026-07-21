from django.contrib import admin
from .models import Category, ProductType, Product, Attribute, AttributeValue, ProductAttributeValue
from django.forms.models import BaseInlineFormSet
from django import forms



class ProductAttributeValueInlineForm(forms.ModelForm):
    class Meta:
        model = ProductAttributeValue
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attribute_value'].required = False


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category_name',
        'slug',
        'category_friendly_name',
    ]

    ordering = ['category_name']


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [
        'product_type',
        'category',
        'slug',
        'product_type_friendly_name',
    ]

    ordering = ['product_type']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            kwargs['queryset'] = Category.objects.order_by('category_name')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ProductAttributeValueInlineFormSet(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        initial = []

        if instance and instance.pk:
            existing_attributes = set(
                instance.productattributevalue_set.values_list(
                    'attribute_id', flat=True
                )
            )

            missing_attributes = Attribute.objects.filter(
                product_type=instance.product_type
            ).exclude(id__in=existing_attributes)

            initial = [
                {'attribute': attribute.id}
                for attribute in missing_attributes
            ]

        kwargs['initial'] = initial
        super().__init__(*args, **kwargs)


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    formset = ProductAttributeValueInlineFormSet
    form = ProductAttributeValueInlineForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        ''' Overides formfield_for_foreighnkey to order the dropdowns in alphebetical order. '''
        if db_field.name == 'attribute':
            kwargs['queryset'] = Attribute.objects.order_by('attribute')
        if db_field.name == 'attribute_value':
            kwargs['queryset'] = AttributeValue.objects.order_by('attribute_value')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_extra(self, request, obj=None, **kwargs):
        if not obj or not obj.pk:
            return 0
        existing_attributes = set(
            obj.productattributevalue_set.values_list('attribute_id', flat=True)
        )
        return Attribute.objects.filter(
            product_type=obj.product_type
        ).exclude(id__in=existing_attributes).count()
    


class ProductAdmin(admin.ModelAdmin):
    fields = [
        'image',
        'product_name',
        'stock',
        'price',
        'brand',
        'description',
        'product_type',
    ]

    exclude = [
        'sku',
        'available',
        'slug',
        'rating',
        'imageURL',
    ]

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

    list_display_links = ['product_name']

    inlines = [
        ProductAttributeValueInline,
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        '''Overides formfield_for_foreighnkey to order the dropdowns in alphebetical order.'''
        if db_field.name == 'product_type':
            kwargs['queryset'] = ProductType.objects.order_by('product_type')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_formset(self, request, form, formset, change):
        if formset.model is not ProductAttributeValue:
            return super().save_formset(request, form, formset, change)
 
        instances = formset.save(commit=False)
 
        # Rows the user ticked "Delete" on
        for obj in formset.deleted_objects:
            obj.delete()
 
        for instance in instances:
            if instance.attribute_value_id:
                # A value was picked - save it
                instance.product = form.instance
                instance.save()
            elif instance.pk:
                # Previously saved row, value has been cleared - remove it
                instance.delete()
            # else: brand-new row with no value selected - skip, don't save
 
        formset.save_m2m()

    class Media:
        js = (
            'products/js/admin_attributes.js',
        )

class AttributeAdmin(admin.ModelAdmin):
    list_display = [
        'attribute', 
        'product_type',
        'attribute_friendly_name',
        'value_type',
    ]

    ordering = ['attribute']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'product_type':
            kwargs['queryset'] = ProductType.objects.order_by('product_type')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AttributeValueAdmin(admin.ModelAdmin):
    list_display = [
        'attribute_value',
        'attribute',
    ]

    ordering = ['attribute__attribute']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'attribute':
            kwargs['queryset'] = Attribute.objects.order_by('attribute')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(AttributeValue, AttributeValueAdmin)