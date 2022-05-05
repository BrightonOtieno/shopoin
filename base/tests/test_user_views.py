from django.test import TestCase
import pytest
from base.models import Product
from django.contrib.auth.models import User
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django.test import TestCase
pytestmark = pytest.mark.django_db

class TestProductsAPIViews(TestCase):

    def setUp(self):
        self.client = APIClient()
        # default user
        self.user = mixer.blend(User,email="testuser@company.com",password="testuser1234", username="testuser@company.com")
        
    # REGISTER USER
    def testRegisterUser(self):
        user1 = {
            "name":"test user1",
            "email":"testuser1@company.com",
            "password":"testuser1234"
        }
        url = reverse("register")
        # http://localhost:8000/api/products/top/
        response = self.client.post(url,user1)
        print(dir(response))
        print(response.json())

        assert response.json() != None
        assert response.status_code == 200

    # LOGIN USER
    def testLoginUser(self):
        """pass in details of user that has already been created (in setup)"""

        response = self.client.login(username=self.user.username, password=self.user.password)
    