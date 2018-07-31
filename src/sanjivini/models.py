from django.db import models

# Create your models here.


class Client(models.Model):

	device_id = models.CharField(max_length=15,unique=True)
	device_secret = models.CharField(max_length=16 , unique=True)



	def __str__(self):
		return self.client_name