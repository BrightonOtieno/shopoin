from unicodedata import name
from django.test import TestCase
import pytest
from base.models import Product
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django.test import TestCase
from django.contrib.auth.models import User
pytestmark = pytest.mark.django_db

class TestProductsAPIViews(TestCase):

    def setUp(self):
        self.client = APIClient()
        # default user
        self.user = mixer.blend(User)

        # create a product
        product = mixer.blend(Product)


    def testGetTopProducts(self):
        # call the url in reverse call
            # reverse url --> use url-name ,
            # when paths changed doesnt affect test
        url = reverse("top-products")
        # http://localhost:8000/api/products/top/
        response = self.client.get(url)
        print(dir(response))



        # assertions
        # - json 
        # - status code
        # headers
        #  -cookies
        assert response.json() != None
        assert response.status_code == 200

    def testGetProducts(self):

        url = reverse("products")
        response = self.client.get(url)
        # print(dir(response))
        
        # assertions
        assert response.json() != None
        assert response.status_code == 200

    # DETAILS 
    def testGetProduct(self):
        # Create Product
        product1 = mixer.blend(Product, name="airpod")
        product2 = mixer.blend(Product)
        url = reverse("product",kwargs={"pk":1})

        response = self.client.get(url)
        print(response.json())
        
        # assertions
        assert response.json() != None
        assert response.json()["_id"] == 1
        assert response.status_code == 200


    # login user not admin can not delete product
    def testDeleteProduct(self):
        #Create Product
        user1 = {
            "name":"test user1",
            "email":"testuser1@company.com",
            "password":"testuser1234"
        }
        url = reverse("register")
        # http://localhost:8000/api/products/top/
        user_response = self.client.post(url,user1)
        
        token = user_response.json()['token']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        product2 = mixer.blend(Product,name="roller-blade")
        url = reverse("product-delete",kwargs={"pk":1})

    
        product_response = self.client.delete(url)

        assert product_response.json() != None
        print(product_response.json())
        print(token)
        assert product_response.json()['detail'] == 'You do not have permission to perform this action.'
        # assert product_response.status_code == 200
        
        
        

































# ADMIN ROUTES
    # def testCreateProduct(self):
    #     product1 = {
    #         "name":"earphone",
    #         "brand":"apple",
    #         "category":"electronic",
    #         "description":"Best product ever",
    #         "raring":3,
    #         "countInStock":10,
    #         "numReviews":10,
    #         "price":100,
    #     }

    #     url = reverse("product-create")
    #     # http://localhost:8000/api/products/top/
    #     response = self.client.post(url,product1)
    #     print(dir(response))

    #     assert response.json() != None
    #     assert response.status_code == 201

