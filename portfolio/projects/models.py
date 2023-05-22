from django.db import models
from datetime import date

# Create your models here.

class Projets(models.Model):

	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to="uploads")
	time  = models.DateField(auto_now_add=True)

	def __str__(self):
		return "%s - %s" % (self.name, self.time)
