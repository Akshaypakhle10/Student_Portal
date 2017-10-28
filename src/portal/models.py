from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Assignments(models.Model):
    Title = models.CharField(default='Title', max_length=50)
    file = models.FileField(default='FileField')
    timestamp = models.DateTimeField( auto_now_add=True)
    def __str__(self):  # __unicode__ for Python 2
        return self.Title

class Lab_Manuals(models.Model):
    Title = models.CharField(default='Title', max_length=50)
    file = models.FileField(default='FileField')
    timestamp = models.DateTimeField( auto_now_add=True)
    def __str__(self):  # __unicode__ for Python 2
        return self.Title


class Reference_Material(models.Model):
    Title = models.CharField(default='Title', max_length=50)
    file = models.FileField(default='FileField')
    timestamp = models.DateTimeField( auto_now_add=True)
    Author = models.CharField(default='Anonymous', max_length=30)
    Image = models.ImageField(default='None',upload_to=None, height_field=None, width_field=None, max_length=100)
    def __str__(self):  # __unicode__ for Python 2
        return self.Title

class Sample_Papers(models.Model):
    Title = models.CharField(default='Title', max_length=50)
    file = models.FileField(default='FileField')
    timestamp = models.DateTimeField( auto_now_add=True)
    def __str__(self):  # __unicode__ for Python 2
        return self.Title

class Timetable(models.Model):
    Title = models.CharField(default='Title', max_length=50)
    file = models.FileField(default='FileField')
    timestamp = models.DateTimeField( auto_now_add=True)
    Div = models.CharField(default='Anonymous', max_length=30)
    Image = models.ImageField(default='None',upload_to=None, height_field=None, width_field=None, max_length=100)
    def __str__(self):  # __unicode__ for Python 2
        return self.Title