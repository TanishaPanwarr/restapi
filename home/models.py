from operator import mod
from unicodedata import name
from django.db import models
class Mobproduct(models.Model):
    name=models.CharField(max_length=20)
    prize=models.IntegerField(max_length=30)
    ram=models.CharField(max_length=20)
    rom=models.CharField(max_length=20)
  
# Create your models here.
