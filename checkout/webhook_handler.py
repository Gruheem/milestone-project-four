import json
from django.http import HttpResponse
from django.conf import settings
from requests import session

from .models import Order, OrderLineItem
from products.models import Product


class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    #  Handles all other webhook events that we do not explicitly handle. 
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    # Handles our checkout.session.completed webhook from Stripe
    def handle_checkout_session_completed(self, event):
        """
        Handle the checkout.session.completed webhook from Stripe and use it to create an order in the database and return info to the chekcout_return page
        """
        session = event['data']['object']
        pid = session['payment_intent']
        # Unpacks the contents of the bag and order form from the metadata in the session object sent off with checkout.session creation
        bag = json.loads(session['metadata']['bag'])
        order_data = json.loads(session['metadata']['order_form'])

        # Check if the order already exists in the database to avoid duplicates incase of multiple webhook events. e.g. server timeout, network issues, sent mid-deployment.
        if Order.objects.filter(stripe_pid=pid).exists():
            return HttpResponse(
                content=f"Webhook received: {event['type']} | order already in database",
                status=200,
            )

        # Sets the field values for the order model 
        order = Order.objects.create(
            stripe_pid=pid,
            full_name=order_data['full_name'],
            email=order_data['email'],
            phone_number=order_data['phone_number'],
            country=order_data['country'],
            postcode=order_data.get('postcode', ''),
            town_or_city=order_data['town_or_city'],
            street_address1=order_data['street_address1'],
            street_address2=order_data.get('street_address2', ''),
            county=order_data.get('county', ''),
        )

        # Iterates through the unpacked bag items to create an order line item for each product
        for item_id, quantity in bag.items():
            product = Product.objects.get(pk=item_id)
            OrderLineItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
            )

        # Updates the order total and delivery cost based on the line items, called from the order model method update_total()
        order.update_total()

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    # Logs the bags of expired sessions to possibly track cart abandonment/help with stock management.
    def handle_checkout_session_expired(self, event):
        session = event['data']['object']
        
        try:
            bag = json.loads(session['metadata']['bag'])
        except (KeyError, TypeError):
            bag = {}  

        print(f"Checkout session expired: {session['id']} | bag contents: {bag}")
        
        return HttpResponse(
            content=f"Webhook received: {event['type']} | session expired, no order created",
            status=200,
        )