from itertools import product
from django.test import TestCase
from base.models import Product, Order,OrderItem, ShippingAddress
from django.contrib.auth.models import User
from mixer.backend.django import mixer
class ProductTest(TestCase):
        def setUp(self):
            # User
            self.user1 = mixer.blend(User,email="testuser@company.com")
            # Order
            self.order1 = mixer.blend(Order, user=self.user1)
            # Product
            self.product1 = mixer.blend(Product, name="earphone")

        def test_order_model_creation(self):
            myOrder = self.order1
            self.assertTrue(isinstance(myOrder,Order))
            self.assertEqual(str(myOrder), self.user1.username)


        def test_order_item_model_creation(self):
            myOrderItem = mixer.blend(OrderItem,product=self.product1, order=self.order1,name=self.product1.name)
            self.assertTrue(isinstance(myOrderItem,OrderItem))
            self.assertEqual(str(myOrderItem), self.product1.name)


        def test_shipping_address_model_creation(self):
            myAddress = mixer.blend(ShippingAddress,order=self.order1,city='Nairobi', country="Kenya")
            self.assertTrue(isinstance(myAddress,ShippingAddress))
            self.assertEqual(str(myAddress), self.order1.user.username)
            # end of tests