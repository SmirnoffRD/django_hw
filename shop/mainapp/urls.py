from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mainapp.views import contact_view, main_view, products_view
from mainapp.models import Category

app_name = 'mainapp'

categories = Category.objects.all()
urlpatterns = [
    path('', main_view, name='main'),
    path('contacts/', contact_view, name='contacts'),
    path('products/<str:pk>/', products_view, name='products'),
]