from django.test import TestCase

class Fitur1UnitTest(TestCase):

	def test_model_can_create_new_tanggapan(self):
        #Creating a new activity
		new_s = Tanggapan.objects.create(tanggapanTwitter="halo", tanggapanSkype="hai", created_date_Twitter = datetime.now(), created_date_Skype=datetime.now())

		#Retrieving all available activity
		counting_all_status= Status.objects.all().count()
		self.assertEqual(counting_all_status,1)

	def test_form_status_input_has_placeholder_and_css_classes(self):
		form = Message_Form()
		self.assertIn('class="todo-status-textarea', form.as_p())
		self.assertIn('id="id_description', form.as_p())

	def test_form_validation_for_blank_items(self):
		form = Message_Form(data={'description':''})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['description'],["This field is required."])
