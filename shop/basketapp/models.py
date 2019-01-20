"""
basket and order item models
"""

from django.db import models
from django.conf import settings
from mainapp.models import Product
# Create your models here.



class Basket(models.Model):
    """
    basket - users basket obj, got OneToOne with OrderItem
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)

    def totall_quantity(self):
        """
        returns totall quantity of all products
        in basket (int)
        """
        _items = OrderItem.objects.filter(basket=self)
        return sum(list(map(lambda x: x.quantity, _items)))


    def totall_price(self):
        """
        returns totall price of basket (int)
        """
        _items = OrderItem.objects.filter(basket=self)
        _summ = 0
        for _item in _items:
            _summ = _summ + _item.totall_price
        return _summ

    def types_quantity(self):
        _items = OrderItem.objects.filter(basket=self)
        return len(_items)




class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)

    @property
    def totall_price(self):
        return self.product.price * self.quantity
