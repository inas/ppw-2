from django.db import models

# Create your models here.
class Tanggapan (models.Model) :
	tanggapanTwitter = models.TextField()
	tanggapanSkype = models.TextField()
	created_date_Twitter = models.DateTimeField(auto_now_add=True)
	created_date_Skype = models.DateTimeField(auto_now_add=True)