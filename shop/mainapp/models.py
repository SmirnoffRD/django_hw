from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название')
    descrition = models.TextField(verbose_name='Описание товара')
    price = models.PositiveIntegerField(verbose_name='Цена')
# class Product_Type(models.Model):
#     pass