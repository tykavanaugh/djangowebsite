from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.TextField()
	link = models.TextField()
	summary = models.TextField()
	description = models.TextField()