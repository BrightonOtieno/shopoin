from django.test import TestCase
from base.models import Product, Order
from django.contrib.auth.models import User
from mixer.backend.django import mixer
class ProductTest(TestCase):
        def setUp(self):
            self.user1 = mixer.blend(User,email="testuser@company.com")
            self.order1 = mixer.blend(Order, user=self.user1)

        def test_order_model_creation(self):
            myOrder = self.order1
            self.assertTrue(isinstance(myOrder,Order))
            self.assertEqual(str(myOrder), self.user1.username)