from django.db import models

# Create your models here.
class JobModel(models.Model):
	title = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	description = models.TextField()
	field = models.CharField(max_length=100)
	url = models.URLField()


	def __str__(self):
		return self.title

