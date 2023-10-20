# <appname>/models.py

from django.db import models

# Create your models here.

class MyCarModel(models.Model):

  make = models.CharField(max_length = 200)
  model = models.CharField(max_length = 200)
  year = models.CharField(max_length = 200)
  nickname = models.CharField(max_length = 200)
  

  def __str__(self):
    return self.title
  




