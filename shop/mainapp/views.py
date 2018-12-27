from django.shortcuts import render, get_object_or_404
from shop.settings import STATICFILES_DIRS
import json
import os
from .models import Category, Product
from django.urls import reverse
from basketapp.models import Basket, OrderItem





# Create your views here.
def main_view(request):
    
    return render(request, 'mainapp/index.html')

def contact_view(request):
    path = os.path.join(STATICFILES_DIRS[0], 'contacts.json')
    with open(path) as data:
        cont_info = json.load(data)

    return render(request, 'mainapp/contact.html', {"continfo": cont_info,})

def products_view(request, pk):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)[0]
        if not basket:
            basket = Basket(user=request.user)
            basket.save()
        basket_items = OrderItem.objects.filter(basket=basket)
        if basket_items:
            types_of_products = len(basket_items)
            sum_of_products = 0
            price_of_products = 0
            for item in basket_items:
                sum_of_products += item.quantity
                price_of_products += item.product.price

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
        'basket': basket,
        "types_of_products": types_of_products,
        "sum_of_products": sum_of_products,
        "price_of_products": price_of_products
    }

    return render(request, 'mainapp/products.html', content)
    
