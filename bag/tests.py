from django.test import TestCase
from django.urls import reverse

from products.models import Category, Product, ProductType


class TestBagViews(TestCase):
    # Assert
    def setUp(self):
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

    def test_adjust_bag_caps_quantity_at_99(self):
        # Arrange - create the test session bag
        session = self.client.session
        session['bag'] = {str(self.product.id): 1}
        session.save()

        # Act - make a POST request with an over-limit quantity
        response = self.client.post(
            reverse('adjust_bag', args=[self.product.id]),
            {'quantity': 500}
        )

        # Assert - bag should be capped at 99, not 500
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 99)

    def test_add_to_bag_caps_quantity_at_99(self):
            # Arrange - create the test session bag
            session = self.client.session
            session['bag'] = {str(self.product.id): 1}
            session.save()
    
            # Act - make a POST request `with an over-limit quantity
            response = self.client.post(
                reverse('add_to_bag', args=[self.product.id]),
                {
                    'quantity': 500,
                    'redirect_url': reverse('view_bag')
                }
            )
    
            # Assert - bag should be capped at 99
            self.assertEqual(self.client.session['bag'][str(self.product.id)], 99)


