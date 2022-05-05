from django.test import TestCase
from base.models import Product
from django.contrib.auth.models import User
# Create your tests here.

class UserTest(TestCase):
    
    def setUp(self):
        self.john = User.objects.create(username="johnTest",email="johntest@company.com", password="john123")
    
    def test_user_model_creation(self):
        d = self.john
        self.assertTrue(isinstance(d,User))
        self.assertEqual(str(d), "johntest@company.com")

