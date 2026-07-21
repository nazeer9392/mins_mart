
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User 

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    image=models.ImageField(default=None)
    desc=models.TextField(max_length=600)
    created_at = models.DateTimeField(default=now())
    
    def  __str__(self):
        return self.name
    
    
class Cart(models.Model):
    name = models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    image=models.ImageField(default=None)
    desc=models.TextField(max_length=600)
    quantity=models.IntegerField(default=1)
    totalprice =models.IntegerField(default=0)
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    