from django.test import TestCase
from base.models import Product
from django.contrib.auth.models import User

class ProductTest(TestCase):
        def setUp(self):
            
            self.product1 = Product.objects.create(name="Airpod", brand="Apple",category="electronic",rating=3.5, numReviews=10, price=100, countInStock=13, description="Best product ever")

        def test_user_model_creation(self):
            airpod = self.product1
            self.assertTrue(isinstance(airpod,Product))
            self.assertEqual(str(airpod), "Airpod")