from django.db import models

# Create your models here.
class Attorney(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    absolutejob = models.CharField(max_length=40)
    biography = models.TextField()
    image = models.ImageField()