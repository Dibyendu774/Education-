from django.db import models

# Create your models here.

class Admin(models.Model):
    objects = None
    Email = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)