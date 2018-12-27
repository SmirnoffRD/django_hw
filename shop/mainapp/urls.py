from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainapp.views import contact_view, main_view, products_view

app_name = 'mainapp'

urlpatterns = [
    path('', main_view, name='main'),
    path('contacts/', contact_view, name='contacts'),
    path('products/<int:pk>/', products_view, name='products'),
]