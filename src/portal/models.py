from django.db import models

# Create your models here.
class portal(models.Model):
	name1 = models.CharField(max_length=20)
	description = models.TextField(default='desc def text')

	def __str__(self):
		return self.name1
