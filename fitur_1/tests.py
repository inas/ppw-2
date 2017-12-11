from django.test import TestCase
from django.test import Client
from django.urls import resolve

# Create your tests here.

class UnitTest(TestCase):
    def test_fitur_1_url_exists(self):
        response = Client().get('/fitur-1/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_landing_page_to_login_page(self):
    	response= Client().get('/')
    	self.assertEqual(response.status_code, 302)