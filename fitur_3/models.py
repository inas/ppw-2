from django.db import models

class Message(models.Model):
	pengguna = models.CharField(max_length=100, null=True, default='not-set')
	title = models.CharField(max_length=140, null=True, default='not-set')
	message = models.TextField(null=True)
	created_date = models.DateTimeField(auto_now_add=True, null=True)

	# , default='not-set', unique=True
