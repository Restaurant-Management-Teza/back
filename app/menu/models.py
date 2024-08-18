from django.db import models

class Product(models.Model):
    class Category(models.TextChoices):
        OOD = 'FD', 'Food'
        DRINKS = 'DR', 'Drinks'
        APPETIZER = 'APP', 'Appetizer'
        MAIN_COURSE = 'MAIN', 'Main Course'
        DESSERT = 'DES', 'Dessert'
        BEVERAGE = 'BEV', 'Beverage'
        SALAD = 'SAL', 'Salad'
        SIDE_DISH = 'SIDE', 'Side Dish'

    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(
        max_length=10,
        choices=Category.choices,
        default=Category.MAIN_COURSE
    )

