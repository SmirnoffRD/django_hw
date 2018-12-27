
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from authapp.models import Custom_User
from .models import Basket, OrderItem
from mainapp.models import Product

# Create your views here.
def basket_view(request):
    basket = Basket.objects.filter(user=request.user)
    if not basket:
        basket = Basket(user=request.user)
        basket.save()

    content = {"basket":basket[0]}
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    basket = Basket.objects.filter(user=request.user)[0]
    if not basket:
        basket = Basket(user=request.user)
        basket.save()

    product = get_object_or_404(Product, pk=pk)
    old_basket_item = OrderItem.objects.filter(basket=basket, product=product)
    if old_basket_item:
        old_basket_item[0].quantity += 1
        old_basket_item[0].save()
    else:
        new_basket_item = OrderItem(basket=basket, product=product)
        new_basket_item.quantity += 1
        new_basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    basket = Basket.objects.filter(user=request.user)

    product = get_object_or_404(Product, pk=pk)

    old_basket_item = OrderItem.objects.filter(basket=basket, product=product)
    old_basket_item[0].quantity -= 1
    old_basket_item[0].save()
    if old_basket_item[0].quantity == 0:
        old_basket_item[0].delete()
        old_basket_item[0].save()
    content ={"basket":basket[0]}
    return render(request, 'basketapp/basket.html', content)