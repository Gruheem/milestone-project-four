import json

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from products.models import Category, Product, ProductType
from checkout.models import Order, OrderLineItem, OrderLineItem

from .webhook_handler import StripeWH_Handler


class TestStripeWebhookHandler(TestCase):

    def setUp(self):
        # Create a test product for the order line item
        self.category = Category.objects.create(
            category_name="Test Category"
        )

        self.product_type = ProductType.objects.create(
            category=self.category,
            product_type="Test Product Type"
        )

        self.product = Product.objects.create(
            product_type=self.product_type,
            product_name="Test Product",
            description="Test Description",
            price=10.00,
            brand="Test Brand",
        )

        # Create a request for the webhook handler
        self.request = RequestFactory().post(
            "/checkout/wh/",
            content_type="application/json",
        )

    def test_duplicate_checkout_webhook_does_not_create_duplicate_order(self):
        # Arrange - create a test event payload for a completed checkout session
        event = {
            "type": "checkout.session.completed",
            "data": {
                "object": {
                    "payment_intent": "pi_test_duplicate",
                    "metadata": {
                        "bag": json.dumps({
                            str(self.product.id): 1,
                        }),
                        "order_form": json.dumps({
                            "full_name": "Test User",
                            "email": "test@example.com",
                            "phone_number": "01234567890",
                            "country": "GB",
                            "postcode": "BS1 1AA",
                            "town_or_city": "Bristol",
                            "street_address1": "1 Test Street",
                            "street_address2": "",
                            "county": "",
                        }),
                        "username": "AnonymousUser",
                        "save_info": "",
                    },
                }
            },
        }

        handler = StripeWH_Handler(self.request)

        # Act - sends two identical webhook events
        handler.handle_checkout_session_completed(event)
        handler.handle_checkout_session_completed(event)

        # Assert - only one order should be created in the database
        self.assertEqual(
            Order.objects.filter(stripe_pid="pi_test_duplicate").count(),
            1,
        )

    def test_unhandled_webhook_event_returns_200(self):
        # Arrange - create a test event payload for an unhandled webhook event
        event = {"type": "some.unknown.event"}
        handler = StripeWH_Handler(self.request)

        # Act - send the unhandled webhook event to the handler
        response = handler.handle_event(event)

        #Assert - response status code should be 200
        self.assertEqual(response.status_code, 200)

    # Tests to see if our order calculates correctly, uses product from existing setUp
    def test_order_total_is_calculated_correctly(self):
        # Arrange - create an order with a line item
        order = Order.objects.create(
            stripe_pid="pi_test",
            full_name="Test User",
            email="test@example.com",
            phone_number="01234567890",
            country="GB",
            postcode="BS1 1AA",
            town_or_city="Bristol",
            street_address1="1 Test Street",
        )
    
        OrderLineItem.objects.create(
            order=order,
            product=self.product,
            quantity=2,
        )

        # Act - calculate the order total
        order.update_total()

        # Assert - the order total should be equal to the product price multiplied by the quantity e.g. 10.00 * 2 = 20.00
        self.assertEqual(order.order_total, 20.00)