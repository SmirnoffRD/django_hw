from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название')

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название')
    descrition = models.TextField(verbose_name='Описание товара')
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products', verbose_name='Изображение', null=True, blank=True)

    def __str__(self):
        return self.name

