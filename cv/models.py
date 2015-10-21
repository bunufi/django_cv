from django.db import models

class Profile(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	address = models.CharField(max_length=200, help_text="test")
	telephone = models.CharField(max_length=200)
	email = models.EmailField(max_length=75)

class Content(models.Model):
	category = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	entry = models.TextField()
	name = models.CharField(max_length=200, blank=True)