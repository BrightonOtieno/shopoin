# import pytest 

# # APIClient allows for api calls
# from rest_framework.test import APIClient

# client = APIClient()

# # from django.test import Client
# client = APIClient()




# @pytest.mark.django_db
# def test_register_user():
#     """ when user registered successfully their data is returned as response"""
#     payload = dict(
#         first_name = "johnterry",
#         username = "johnterry",
#         email = 'john@company.com',
#         password = "john1234"

#     )

#     data = client.post('api/users/register/',payload, format='json')

#     print(dir(data), "response")
#     # print(data['status_code'], "CODE")
    


# @pytest.mark.django_db
# def test_login_user(user):
#     """ when user loggedin successfully their data is returned as response"""
#     payload = dict(
        
#         email = 'john@company.com',
#         password = "john1234"

#     )

#     response = client.post('api/users/login/',payload, format='json')

#     # data = response.data
#     # assert response.status_code == 404

# TESTING URLS

# import pytest 
# from 

# class TestProduct
