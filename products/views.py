from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Prefetch

from .models import Attribute, AttributeValue, Product, ProductType


def get_attributes(request):
    ''' Retrieves Attribute list as JSON for the list of possible Attributes when Adding a Product on the Product Admin '''
    product_type_id = request.GET.get("product_type_id")

    attributes = Attribute.objects.filter(product_type_id=product_type_id).values(
        "id",
        "attribute"
    )

    return JsonResponse(
        list(attributes),
        safe=False
    )

def get_attribute_values(request):
    ''' Retrieves Attributes Values as JSON for the Attributes Value Dropdowns Assigning Attributes and values in the Products Admin '''
    attribute_id = request.GET.get("attribute_id")

    values = AttributeValue.objects.filter(attribute_id=attribute_id).values(
        "id",
        "attribute_value"
    )

    return JsonResponse(
        list(values),
        safe=False
    )

def all_products(request):
    ''' Functin to return Products for the Products Page '''
    products = Product.objects.all()

    product_types = None
    attributes = None

    if request.GET:
        if 'product_types' in request.GET:
            product_types = request.GET['product_types'].split(',')
            products = products.filter(product_type__slug__in=product_types)
            product_types = ProductType.objects.filter(slug__in=product_types)
            
            # This fetches only the attributes that have values and only the values ghat have been assigned to an available product
            attributes = Attribute.objects.filter(
                product_type__in=product_types,
                values__productattributevalue__product__in=products
            ).distinct().prefetch_related(
                Prefetch(
                    'values',
                    queryset=AttributeValue.objects.filter(
                        productattributevalue__product__in=products
                    ).distinct()
                )
            )

    context = {
        'products' : products,
        'current_product_types' : product_types,
        'attributes' : attributes,
    }

    return render(request, 'products/products.html', context)