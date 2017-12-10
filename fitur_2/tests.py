from django.test import TestCase
from django.test import Client
from django.urls import resolve

# Create your tests here.

class fitur2UnitTest(TestCase):
    def test_fitur_2_url_is_exist(self):
        response = Client().get('/fitur-2/')
        self.assertEqual(response.status_code, 200)