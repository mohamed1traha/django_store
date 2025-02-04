from django.db import models
from django.contrib.sessions.models import Session
from django_stor import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    featured = models.BooleanField(default=True)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=500, unique=True)
    bio = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_description = models.TextField(null=True)
    description = models.TextField(null=True)
    pdf_file = models.FileField(null=True)
    image = models.ImageField()
    price = models.FloatField()
    featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL , null=True)
    
    @property
    def pdf_file_url(self):
        if self.pdf_file:
            return settings.SITE_URL + self.pdf_file.url
        return None

    def __str__(self): 
        return self.name
from checkout.models import Transaction

class Order(models.Model):
    transaction =models.OneToOneField(Transaction,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)




    def __str__(self): 
        return str(self.id)
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    items = models.JSONField(default=dict)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)


class Slider(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(max_length=500)
    image = models.ImageField(null=True)
    order =  models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.title
    

    






