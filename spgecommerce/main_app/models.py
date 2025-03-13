from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

#class Customer(models.Model):

#class Product(models.Model):

#class Order(models.Model):