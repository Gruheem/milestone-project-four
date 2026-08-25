from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from products.models import Product


# Create your views here.
def view_bag(request):
    """A view to return the bag page"""

    return render(request, "bag/bag.html")

def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    bag = request.session.get("bag", {})

    item_id = str(item_id)

    if item_id in bag:
        bag[item_id] += min(quantity, 98)
        messages.success(
            request, f"Updated {product.product_name} quantity to {bag[item_id]}."
        )
    else:
        bag[item_id] = min(quantity, 98)
        messages.success(request, f"{product.product_name} has been added to your bag.")

    request.session["bag"] = bag

    print(request.session["bag"])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product in the shopping bag"""

    quantity = int(request.POST.get("quantity"))
    product = get_object_or_404(Product, pk=item_id)

    bag = request.session.get("bag", {})

    if quantity >= 1:
        bag[item_id] = min(quantity, 99)
        messages.success(
            request, f"Updated {product.product_name} quantity to {bag[item_id]}."
        )

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """Remove the specified product from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get("bag", {})

    # Convert item_id into a string to match the data stored in the
    # session bag dictionary.
    item_id = str(item_id)

    if item_id in bag:
        bag.pop(item_id)
        messages.success(request, f"Removed {product.product_name} from your bag.")

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))
