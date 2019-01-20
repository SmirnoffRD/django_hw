
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product
from mainapp.views import get_basket
from .models import OrderItem


# Create your views here.
def basket_view(request):
    basket = get_basket(user=request.user)
    items = OrderItem.objects.filter(basket=basket)
    content = {"basket":basket, "items":items,}
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    basket = get_basket(user=request.user)

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
    basket = get_basket(user=request.user)
    print(pk)
    product = get_object_or_404(Product, pk=pk)

    old_basket_item = OrderItem.objects.filter(basket=basket, product=product)
    if not old_basket_item:
        pass
    else:
        if old_basket_item[0].quantity == 1:
            old_basket_item.delete()
        else:
            old_basket_item[0].quantity -= 1
            old_basket_item[0].save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_remove_all(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = get_basket(user=request.user)
    basket_item = OrderItem.objects.filter(basket=basket, product=product)
    print(basket_item)
    basket_item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
