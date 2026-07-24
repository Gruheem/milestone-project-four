from django.http import JsonResponse
from django.shortcuts import render
from .models import Attribute, AttributeValue, Product


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

    context = {
        'products' : products
    }

    return render(request, 'products/products.html', context)