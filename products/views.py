from django.db.models.functions import Lower
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
    sort = None
    direction = None

    if request.GET:
        # Product Sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            # This is a special case for sorting by product_name as we want to ignore case sensitivity when sorting by name.
            if sortkey == 'product_name':
                sortkey = 'lower_product_name'
                products = products.annotate(
                    lower_product_name=Lower('product_name')
                )

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'product_types' in request.GET:
            # Parses the Product Types into list
            product_types = request.GET['product_types'].split(',')
            # Filters the Products by Product Type
            products = products.filter(product_type__slug__in=product_types)
            # Turns the Product typ list into a list of ProductType table Objects
            product_types = ProductType.objects.filter(slug__in=product_types)

            # Captures a product list for the filters
            available_filter_products = products

        # Search bar filtering
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please Enter Your Search Terms")
                return redirect(reverse('products'))
            
            # We search in the product_name and description for the query
            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        # This creates a snpashot of the products after either a search or a product category filter.
        available_filter_products = products

        # Take the key value pairings we have sent across in our URL (iterate over them)
        for key, value in request.GET.items():
            # Ignores product_type key and and q with its respective value as it is the attrribute and value were after
            if key in ('product_types', 'q', 'sort', 'direction'):
                continue

            # Creates a values list from the keys we are iterating over
            values_list = request.GET.getlist(key)
            # Retrieves the products with the Attribute/Value pairing
            products = products.filter(
                productattributevalue__attribute__slug=key,
                productattributevalue__attribute_value__slug__in=values_list
            )

        # This creates a dictionary to remember which key:value pairs we have which allows us to keep the filter checkbox ticked on reload 
        for key in request.GET:
            if key != 'product_types':
                selected_values[key] = request.GET.getlist(key)
        
        # Creates a list of Attributes, and any populated values to populate the filter, uses the available_filter_products snapshot not 
        # products as to not shrink our filter options(as displayed product reduce) when we apply our filter.
        attributes = Attribute.objects.filter(
            values__productattributevalue__product__in=available_filter_products
                   # prefetch_related negated the n + 1 query problem by fetching all value in one extra query
        ).distinct().prefetch_related(
          # Prefetch instructs to only fetch values attatched to the attribute which have existing data in them.
            Prefetch(
                'values',
                queryset=AttributeValue.objects.filter(
                    productattributevalue__product__in=available_filter_products
                ).distinct()
            )
        )

        # Creates an empty ordered dictionary. We use a Dictionary as it deduplicates for us automatically Ordering the 
        # dictionary(explicitly as technically done automaticaly onw) allows ur to reliably iterate over it
        grouped_attributes = OrderedDict()

        # Creates the structure for this dictionary iterating over the attributes to create keys
        for attribute in attributes:
            key = attribute.slug
            if key not in grouped_attributes:
                grouped_attributes[key] = {
                    'name': attribute.attribute_friendly_name,
                    'slug': attribute.slug,
                    'values': {}  # Using a Dictionary here deduplicates the values in the list.
                }
            # Iterates over the attributes again to add values to the keys 
            for value in attribute.values.all():
                grouped_attributes[key]['values'][value.slug] = value

        # Convert each group's values dict into a sorted list for the template to use more easily, as we no longer need to know what the keys are just the values. 
        # Use 'lambda' as the key argument for sorted as it expects a function. We use it to return attribute_value to sort by. 
        for key in grouped_attributes:
            grouped_attributes[key]['values'] = sorted(
                grouped_attributes[key]['values'].values(),
                key=lambda v: v.attribute_value
            )

    current_sorting = f'{sort}_{direction}'

    context = {
        'products' : products,
        'current_product_types' : product_types,
        'attributes' : grouped_attributes.values(),
        'selected_values' : selected_values,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'products/product_detail.html', context)