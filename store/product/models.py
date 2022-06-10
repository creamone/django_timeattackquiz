from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    description = models.CharField()
    price = models.IntegerField()
    stock = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=30)

class OrderStatus(models.Model):
    status = models.CharField(max_length=30)

class ProductOrder(models.Model):