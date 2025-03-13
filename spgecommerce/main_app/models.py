from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.EmailField(max_length=100)
    #password = look at doing this with email hash password tokens?

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    img = models.ImageField(upload_to='uploads/product/')

#class Order(models.Model):