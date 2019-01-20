from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket_view, name='basket'),
    path('edit/<int:pk>/<int:value>/', basketapp.basket_edit, name='product_edit'),
    path('delete/<int:pk>/', basketapp.basket_remove, name='product_remove'),
    path('add/<int:pk>/', basketapp.basket_add, name='product_add'),
    path('delete_all/', basketapp.basket_remove_all, name='product_remove_all'),
]
