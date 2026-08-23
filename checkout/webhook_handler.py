import json

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from requests import session

from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

from .models import Order, OrderLineItem


class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email
        """
        cust_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order},
        )
        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])

    #  Handles all other webhook events that we do not explicitly handle.
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}", status=200
        )

    # Handles our checkout.session.completed webhook from Stripe
    def handle_checkout_session_completed(self, event):
        """
        Handle the checkout.session.completed webhook from Stripe.

        Use it to create an order in the database and return info to the
        checkout return page.
        """
        session = event["data"]["object"]
        pid = session["payment_intent"]
        # Unpack the bag and order form metadata from the Stripe session.
        bag = json.loads(session["metadata"]["bag"])
        order_data = json.loads(session["metadata"]["order_form"])
        username = session["metadata"]["username"]

        # Check if the order already exists to avoid duplicate webhook
        # events.
        if Order.objects.filter(stripe_pid=pid).exists():
            return HttpResponse(
                content=(
                    f"Webhook received: {event['type']} | "
                    "order already in database"
                ),
                status=200,
            )

        # Create profile and save_info variables for later in the function.
        profile = None

        try:
            save_info = session["metadata"]["save_info"]
        except (KeyError, TypeError):
            save_info = ""

        if username != "AnonymousUser":
            try:
                user = User.objects.get(username=username)
                profile = UserProfile.objects.get(user=user)
            except (User.DoesNotExist, UserProfile.DoesNotExist):
                profile = None

        # Set the field values for the order model.
        order = Order.objects.create(
            stripe_pid=pid,
            user_profile=profile,
            full_name=order_data["full_name"],
            email=order_data["email"],
            phone_number=order_data["phone_number"],
            country=order_data["country"],
            postcode=order_data.get("postcode", ""),
            town_or_city=order_data["town_or_city"],
            street_address1=order_data["street_address1"],
            street_address2=order_data.get("street_address2", ""),
            county=order_data.get("county", ""),
        )

        # Save the information from the order if the user is logged in and
        # ticked the save info checkbox.
        if profile and save_info:
            profile_data = {
                "default_full_name": order.full_name,
                "default_phone_number": order.phone_number,
                "default_country": order.country,
                "default_postcode": order.postcode,
                "default_town_or_city": order.town_or_city,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_county": order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

        # Create an order line item for each product in the unpacked bag.
        for item_id, quantity in bag.items():
            product = Product.objects.get(pk=item_id)
            OrderLineItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
            )

        # Update the order total and delivery cost from the order model.
        order.update_total()

        # Sends the confirmation email to the user
        self._send_confirmation_email(order)

        return HttpResponse(
            content=(
                f"Webhook received: {event['type']} | SUCCESS: "
                "Created order in webhook"
            ),
            status=200,
        )

    # Log expired sessions to help track cart abandonment and stock
    # management.
    def handle_checkout_session_expired(self, event):
        session = event["data"]["object"]

        try:
            bag = json.loads(session["metadata"]["bag"])
        except (KeyError, TypeError):
            bag = {}

        print(f"Checkout session expired: {session['id']} | bag contents: {bag}")

        return HttpResponse(
            content=(
                f"Webhook received: {event['type']} | session expired, "
                "no order created"
            ),
            status=200,
        )
