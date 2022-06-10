from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table ="drinks"


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "categories"

