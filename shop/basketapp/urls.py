from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket_view, name='basket'),
    path('add/<int:pk>/', basketapp.basket_add, name='product_add'),
    path('delete/<int:pk>/', basketapp.basket_remove, name='product_remove'),
]