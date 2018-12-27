from django.shortcuts import render, get_object_or_404
from shop.settings import STATICFILES_DIRS
import json
import os
from .models import Category, Product
from django.urls import reverse






# Create your views here.
def main_view(request):
    
    return render(request, 'mainapp/index.html')

def contact_view(request):
    path = os.path.join(STATICFILES_DIRS[0], 'contacts.json')
    with open(path) as data:
        cont_info = json.load(data)

    return render(request, 'mainapp/contact.html', {"continfo": cont_info,})

def products_view(request, pk):
    categories = Category.objects.all()
    if pk == "0":
        products = Product.objects.all().order_by('price')
        category = {'name': 'все'}
    else:
        category = get_object_or_404(Category, pk=pk)
        products = Product.objects.filter(category__pk=pk).order_by('price')
    content = {
        'products': products,
        'category': category,
        'categories': categories
    }

    return render(request, 'mainapp/products.html', content)
    
