from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Prefetch, Q
from collections import OrderedDict


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
    query = None

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

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please Enter Your Search Terms")
                return redirect(reverse('products'))
            
            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        available_filter_products = products

        # Take the key value pairings we have sent across in our URL (iterate over them)
        for key, value in request.GET.items():
            # Ignores product_type key and its value as it is the attrribute and value were after
            if key in ('product_types', 'q'):
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
            values__productattributevalue__product__in=available_filter_products
        ).distinct().prefetch_related(
            Prefetch(
                'values',
                queryset=AttributeValue.objects.filter(
                    productattributevalue__product__in=available_filter_products
                ).distinct()
            )
        )

        grouped_attributes = OrderedDict()

        for attribute in attributes:
            key = attribute.slug
            if key not in grouped_attributes:
                grouped_attributes[key] = {
                    'name': attribute.attribute_friendly_name,
                    'slug': attribute.slug,
                    'values': {}  # keyed by value.slug to dedupe merged values
                }
            for value in attribute.values.all():
                grouped_attributes[key]['values'][value.slug] = value

        # Convert each group's values dict into a sorted list for the template
        for key in grouped_attributes:
            grouped_attributes[key]['values'] = sorted(
                grouped_attributes[key]['values'].values(),
                key=lambda v: v.attribute_value
            )

    context = {
        'products' : products,
        'current_product_types' : product_types,
        'attributes' : grouped_attributes.values(),
        'selected_values' : selected_values,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'products/product_detail.html', context)