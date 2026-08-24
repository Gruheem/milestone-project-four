from collections import OrderedDict

from django.contrib import messages
from django.db.models import Prefetch, Q
from django.db.models.functions import Lower
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Attribute, AttributeValue, Product, ProductType


def get_attributes(request):
    """Return attributes as JSON for the product admin."""
    product_type_id = request.GET.get("product_type_id")

    attributes = Attribute.objects.filter(
        product_type_id=product_type_id
    ).values("id", "attribute")

    return JsonResponse(list(attributes), safe=False)


def get_attribute_values(request):
    """Return attribute values as JSON for the product admin."""
    attribute_id = request.GET.get("attribute_id")

    values = AttributeValue.objects.filter(
        attribute_id=attribute_id
    ).values("id", "attribute_value")

    return JsonResponse(list(values), safe=False)


def all_products(request):
    """Return products for the products page."""
    products = Product.objects.all()

    product_types = None
    attributes = None
    selected_values = {}
    query = None
    sort = None
    direction = None
    category = None
    grouped_attributes = OrderedDict()

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            # Sort by product name without case sensitivity.
            if sortkey == "product_name":
                sortkey = "lower_product_name"
                products = products.annotate(
                    lower_product_name=Lower("product_name")
                )

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "product_types" in request.GET:
            # Parse product types into a list.
            product_types = request.GET["product_types"].split(",")
            # Filter products by product type.
            products = products.filter(product_type__slug__in=product_types)
            # Turn the slug list into ProductType objects.
            product_types = ProductType.objects.filter(slug__in=product_types)
            # Use the first ProductType to determine the category.
            category = product_types.first().category
            available_filter_products = products

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "Please Enter Your Search Terms")
                return redirect(reverse("home"))

            # Search the product name and description.
            queries = (
                Q(product_name__icontains=query)
                | Q(description__icontains=query)
            )
            products = products.filter(queries)

        # Snapshot the products after either a search or a product filter.
        available_filter_products = products

        # Take the key/value pairs sent in the URL.
        for key, value in request.GET.items():
            # Ignore product_types, q, sort, and direction.
            if key in ("product_types", "q", "sort", "direction"):
                continue

            # Build a list of selected values for this attribute.
            values_list = request.GET.getlist(key)
            # Filter products by the attribute/value pairing.
            products = products.filter(
                productattributevalue__attribute__slug=key,
                productattributevalue__attribute_value__slug__in=values_list,
            )

        # Remember the selected values so the filter checkboxes stay ticked
        # on reload.
        for key in request.GET:
            if key != "product_types":
                selected_values[key] = request.GET.getlist(key)

        # Build filter attributes from the available products snapshot so
        # the options do not shrink as results narrow.
        attributes = (
            Attribute.objects.filter(
                values__productattributevalue__product__in=available_filter_products
            )
            .distinct()
            .prefetch_related(
                # Only fetch values attached to attributes that have data.
                Prefetch(
                    "values",
                    queryset=AttributeValue.objects.filter(
                        productattributevalue__product__in=available_filter_products
                    ).distinct(),
                )
            )
        )

        # Build an ordered dictionary so attributes stay deduplicated and
        # predictable when iterated over.
        for attribute in attributes:
            key = attribute.slug
            if key not in grouped_attributes:
                grouped_attributes[key] = {
                    "id": attribute.id,
                    "name": attribute.attribute_friendly_name,
                    "slug": attribute.slug,
                    # Deduplicate values by key.
                    "values": {},
                }
            # Add values to each attribute key.
            for value in attribute.values.all():
                grouped_attributes[key]["values"][value.slug] = value

        # Convert each group's values dict into a sorted list for the
        # template.
        # Use lambda as the sort key so values are ordered by attribute
        # value.
        for key in grouped_attributes:
            grouped_attributes[key]["values"] = sorted(
                grouped_attributes[key]["values"].values(),
                key=lambda v: v.attribute_value,
            )

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "current_product_types": product_types,
        "category": category,
        "attributes": grouped_attributes.values(),
        "selected_values": selected_values,
        "search_term": query,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
