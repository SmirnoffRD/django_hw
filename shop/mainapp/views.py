from django.shortcuts import render
from shop.settings import STATICFILES_DIRS
import json
import os
from .models import Category, Product
from django.urls import reverse

categories = Category.objects.all()





# Create your views here.
def main_view(request):
    content = {
        'categories': categories
    }
    for cat in categories:
        print('nnnnn', cat.pk)
    
    return render(request, 'mainapp/index.html', content)

def contact_view(request):
    path = os.path.join(STATICFILES_DIRS[0], 'contacts.json')
    with open(path) as data:
        cont_info = json.load(data)

    return render(request, 'mainapp/contact.html', {"continfo": cont_info,})

def products_view(request, pk):
    print(pk)
    print(type(pk))
    if pk == "0":
        products = Product.objects.all()
        category = {'name': 'All'}
    else:
        category = Category.objects.get(pk=pk)
        products = Product.objects.filter(category=category)
    content = {
        'products': products,
        'category': category,
        'categories': categories
    }


    print('обновление корзины')
    return render(request, 'mainapp/products.html', content)
    
