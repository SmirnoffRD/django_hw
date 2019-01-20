import json
import os
import random
from django.shortcuts import render, get_object_or_404
from shop.settings import STATICFILES_DIRS
from basketapp.models import Basket, OrderItem
from .models import Category, Product



def get_basket(user):
    if user.is_authenticated:
        basket = Basket.objects.filter(user=user)
        if not basket:
            basket = Basket(user)
            basket.save()
        return basket[0]
    return False

def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]

def get_same_products(product):
    same_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:3]
    return same_products



# Create your views here.
def main_view(request):
    types_of_products = None
    sum_of_products = None
    price_of_products = None
    basket = get_basket(request.user)
    if basket:
        types_of_products = basket.types_quantity
        sum_of_products = basket.totall_quantity
        price_of_products = basket.totall_price
    content = {
        "types_of_products": types_of_products,
        "sum_of_products": sum_of_products,
        "price_of_products": price_of_products
    }
    return render(request, 'mainapp/index.html', content)

def contact_view(request):
    types_of_products = None
    sum_of_products = None
    price_of_products = None
    basket = get_basket(request.user)
    if basket:
        types_of_products = basket.types_quantity
        sum_of_products = basket.totall_quantity
        price_of_products = basket.totall_price
    path = os.path.join(STATICFILES_DIRS[0], 'contacts.json')
    with open(path) as data:
        cont_info = json.load(data)
    content = {
        "continfo": cont_info,
        "types_of_products": types_of_products,
        "sum_of_products": sum_of_products,
        "price_of_products": price_of_products
    }

    return render(request, 'mainapp/contact.html', content)

def products_view(request, pk):
    types_of_products = None
    sum_of_products = None
    price_of_products = None
    basket = get_basket(request.user)
    r_product = get_hot_product()
    if basket:
        types_of_products = basket.types_quantity
        sum_of_products = basket.totall_quantity
        price_of_products = basket.totall_price

    categories = Category.objects.all()
    if pk == 0:
        products = Product.objects.all().order_by('price')
        category = {'name': 'все'}
    else:
        category = get_object_or_404(Category, pk=pk)
        products = Product.objects.filter(category__pk=pk).order_by('price')
    content = {
        'products': products,
        'category': category,
        'categories': categories,
        "types_of_products": types_of_products,
        "sum_of_products": sum_of_products,
        "price_of_products": price_of_products,
        "r_product": r_product,
    }

    return render(request, 'mainapp/products.html', content)

def product_view(request, pk):
    types_of_products = None
    sum_of_products = None
    price_of_products = None
    order_item = None
    basket = get_basket(request.user)
    categories = Category.objects.all()
    product = get_object_or_404(Product, pk=pk)
    if basket:
        types_of_products = basket.types_quantity
        sum_of_products = basket.totall_quantity
        price_of_products = basket.totall_price
        order_item = OrderItem.objects.filter(basket=basket, product=product)

    content = {
        'product': product,
        'categories': categories,
        "types_of_products": types_of_products,
        "sum_of_products": sum_of_products,
        "price_of_products": price_of_products,
        "order_item": order_item,
    }

    return render(request, 'mainapp/product.html', content)
