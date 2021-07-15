from django.db import models

# Create your models here.

class Attorney(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    absolutejob = models.CharField(max_length=40)
    biography = models.TextField()
    image = models.ImageField()
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email= models.EmailField()
    case_details = models.TextField()


class FreeCase(models.Model):
   name = models.CharField(max_length=30)
   email= models.EmailField()
   subject = models.CharField(max_length=30)
   case_details = models.TextField()

class Shop(models.Model):
    stuffname = models.CharField(max_length = 40)
    image = models.ImageField() 
    price = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.BooleanField(blank=True)
    
    
    
    
class ProductDetail(models.Model):
    productname = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    below_description = models.TextField()
    
    
class Reviews(models.Model):
    review = models.TextField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    
