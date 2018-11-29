from django.shortcuts import render
from shop.settings import STATICFILES_DIRS
import json
import os


# Create your views here.
def main_view(request):
    return render(request, 'mainapp/index.html')

def contact_view(request):
    path = os.path.join(STATICFILES_DIRS[0], 'contacts.json')
    with open(path) as data:
        cont_info = json.load(data)

    return render(request, 'mainapp/contact.html', {"continfo": cont_info,})

def products_view(request):
    return render(request, 'mainapp/products.html')