from django.db import models

# Create your models here.
class Project(models.Model):
	Title = models.CharField(default="",max_length = 50)
	Link = models.URLField(default="")
	Summary = models.TextField(default="")
	FullDescription = models.TextField(default="")