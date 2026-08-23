from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from checkout.models import Order

from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    """
    A view to return the profile page
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"

    context = {"form": form, "orders": orders, "on_profile_page": True}

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    A view to return the order history page
    """

    order = get_object_or_404(Order, order_number=order_number)

    if order.user_profile != request.user.userprofile:
        messages.error(request, "That order doesn't belong to your account.")
        return redirect("profile")

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"

    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
