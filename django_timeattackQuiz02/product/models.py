from django.db import models

# one to many 관계
# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "Category"

    category_name = models.CharField(max_length=256)
    category_menu = models.CharField(max_length=256)

class Drink(models.Model):
    class Meta:
        db_table = "Drink"

    drink_name = models.CharField(max_length=256)
    drink_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    drink_nutrition = models.CharField(max_length=256)
    drink_allergy = models.CharField(max_length=256)



