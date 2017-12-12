from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, add_message
from .models import Message
from .forms import Message_Form

# Create your tests here.
class Fitur3UnitTest(TestCase):

	def test_fitur_3_url_exists(self):
		response = Client().get('/fitur-3/')
		self.assertEqual(response.status_code, 200)

	def test_fitur3_using_index_func(self):
		found = resolve('/fitur-3/')
		self.assertEqual(found.func, index)

	# def test_model_can_create_new_status(self):
 #        #Creating a new activity
	# 	new_s = Status.objects.create(status='This is a test')

	# 	#Retrieving all available activity
	# 	counting_all_status= Status.objects.all().count()
	# 	self.assertEqual(counting_all_status,5)

	# def test_status_posted_is_equal_to_written_one(self):
	# 	new_status='hello'
	# 	test_write=Status.objects.create(status=new_status)
	# 	self.assertEqual(str(test_write), new_status)

	# def test_form_status_input_has_placeholder_and_css_classes(self):
	# 	form = Status_Form()
	# 	self.assertIn('class="todo-status-textarea', form.as_p())
	# 	self.assertIn('id="id_description', form.as_p())

	# def test_form_validation_for_blank_items(self):
	# 	form = Status_Form(data={'description':''})
	# 	self.assertFalse(form.is_valid())
	# 	self.assertEqual(form.errors['description'],["This field is required."])

	# def test_fitur5_post_success_and_render_the_result(self):
	# 	test = 'Anonymous'
	# 	response_post = Client().post('/fitur-3/add_status', {'description': test})
	# 	self.assertEqual(response_post.status_code, 302)

	# 	response= Client().get('/fitur-3/')
	# 	html_response = response.content.decode('utf8')
	# 	self.assertIn(test, html_response)

	# def test_fitur5_post_error_and_render_the_result(self):
	# 	test = 'Anonymous'
	# 	response_post = Client().post('/fitur-3/add_message', {'description':''})
	# 	self.assertEqual(response_post.status_code, 302)

	# 	response= Client().get('/fitur-5/')
	# 	html_response = response.content.decode('utf8')
	# 	self.assertNotIn(test, html_response)
