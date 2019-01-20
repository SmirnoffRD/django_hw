from django.urls import path

from mainapp.views import contact_view, main_view, products_view, product_view

app_name = 'mainapp'

urlpatterns = [
    path('', main_view, name='main'),
    path('contacts/', contact_view, name='contacts'),
    path('products/<int:pk>/', products_view, name='products'),
    path('product/<int:pk>/', product_view, name='product'),
]
