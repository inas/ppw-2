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

	def test_landing_page(self):
		#go to log in page if user is not logged in
		response = self.client.get('/fitur-1/')
		html_response = response.content.decode('utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed('fitur_1/fitur_1.html')
		self.assertIn("Login with LinkedIn", html_response)