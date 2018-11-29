from django.shortcuts import render

# Create your views here.
def main_view(request):
    return render(request, 'mainapp/index.html')

def contact_view(request):
    return render(request, 'mainapp/contact.html')

def products_view(request):
    return render(request, 'mainapp/products.html', {'data': 'COOL'})