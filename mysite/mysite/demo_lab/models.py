from django.db import models

class vInfra(models.Model):
	def __str__(self):
		return self.name

	name = models.CharField(max_length=30)
	ip = models.GenericIPAddressField()

class Emails(models.Model):
	def __str__(self):
		return self.email

	email = models.EmailField()

