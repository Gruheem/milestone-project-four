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
    selected_values = {}

    if request.GET:
        if 'product_types' in request.GET:
            # Parses the Product Types into list
            product_types = request.GET['product_types'].split(',')
            # Filters the Products by Product Type
            products = products.filter(product_type__slug__in=product_types)
            # Turns the Product typ list into a list of ProductType table Objects
            product_types = ProductType.objects.filter(slug__in=product_types)

            # Captures a product list for the filters
            available_filter_products = products

            # Take the key value pairings we have sent across in our URL (iterate over them)
            for key, value in request.GET.items():
                # Ignores product_type key and its value as it is the attrribute and value were after
                if key == 'product_types':
                    continue

                # Creates a values list from the keys we are iterating over
                values_list = request.GET.getlist(key)
                # Retrieves the products with the Attribute/Value pairing
                products = products.filter(
                    productattributevalue__attribute__slug=key,
                    productattributevalue__attribute_value__slug__in=values_list
                )

            # Creates a dictionary of attribute:value pairs for us to iterate over for the filter.
            for key in request.GET:
                if key != 'product_types':
                    selected_values[key] = request.GET.getlist(key)
            
            # This fetches the attributes and their values from the all the products in a product type(s)
            attributes = Attribute.objects.filter(
                product_type__in=product_types,
                values__productattributevalue__product__in=available_filter_products
            ).distinct().prefetch_related(
                Prefetch(
                    'values',
                    queryset=AttributeValue.objects.filter(
                        productattributevalue__product__in=available_filter_products
                    ).distinct()
                )
            )

    context = {
        'products' : products,
        'current_product_types' : product_types,
        'attributes' : attributes,
        'selected_values' : selected_values,
    }

    return render(request, 'products/products.html', context)