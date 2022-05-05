from django.test import TestCase
import pytest
from base.models import Product
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django.test import TestCase
pytestmark = pytest.mark.django_db

class TestProductsAPIViews(TestCase):

    def setUp(self):
        self.client = APIClient()
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
        product1 = mixer.blend(Product)
        product2 = mixer.blend(Product)
        url = reverse("product",kwargs={"pk":1})

        response = self.client.get(url)
        
        # assertions
        assert response.json() != None
        assert response.status_code == 200

































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

