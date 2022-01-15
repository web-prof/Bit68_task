import pytest
from django.contrib.auth.models import User
from products.models import Products
from rest_framework.test import APIClient, APITestCase
from mixer.backend.django import mixer
from django.test import TestCase

pytest_mark = pytest.mark.django_db


class Test_Products_APIViews(TestCase):
    def setup(self):
        self.client = APIClient()

    def test_product_list_work(self):
        # create_product
        product = mixer.blend(Products, prd_name='labtop')
        # call the url
        response = self.client.get('/products/')
        # assertion
        assert response.json != None
        assert response.status_code == 200
        assert product.prd_name == 'labtop'


@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user("test_user", "test@gmail.com", "password")
    assert user.username == "test_user"


# class Test_authentication(APITestCase):
#     def authenticate(self):
#         self.client.post(reverse("accounts:register"),{"username":"username","email":"email.gmail.com","password":"password"})
#         response=self.client.post('/api/token/',{"username":"username","password":"password"})
#         self.clien.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")
#         def endpoint_need_auth_to_be_Tested(self):
#             #test the end point here
#             pass
