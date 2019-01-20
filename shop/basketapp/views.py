
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse, Http404, HttpRequest
from mainapp.models import Product
from mainapp.views import get_basket
from .models import OrderItem




# Create your views here.
@login_required
def basket_view(request):
    basket = get_basket(user=request.user)
    items = OrderItem.objects.filter(basket=basket)
    content = {"basket":basket, "items":items,}
    return render(request, 'basketapp/basket.html', content)

@login_required
def basket_edit(request, pk, value=0):
    if request.is_ajax():
        basket = get_basket(user=request.user)
        print('1')
        old_basket_item = get_object_or_404(OrderItem, pk=pk)
        if old_basket_item:
            print('2')
            if value == 0:
                print('3')
                OrderItem.objects.filter(pk=pk).delete()
            else:
                print('4')
                old_basket_item.quantity = value
                old_basket_item.save()
        else:
            print('5')
            product = get_object_or_404(Product, pk=pk)
            new_basket_item = OrderItem(basket=basket, product=product)
            new_basket_item.quantity = 1
            new_basket_item.save()
        items = OrderItem.objects.filter(basket=basket)
        content = {"basket":basket, "items":items,}
        result = render_to_string('basketapp/basket_inc.html', content)
    else:
        return Http404


    return JsonResponse({'result': result})
@login_required
def basket_remove(request, pk):
    basket = get_basket(user=request.user)

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
@login_required
def basket_add(request, pk):
    basket = get_basket(user=request.user)

    product = get_object_or_404(Product, pk=pk)

    old_basket_item = OrderItem.objects.filter(basket=basket, product=product)
    print(old_basket_item)
    if old_basket_item:
        old_basket_item[0].quantity += 1
        old_basket_item[0].save()
        print(old_basket_item[0].quantity)
    else:
        print('not')
        product = get_object_or_404(Product, pk=pk)
        new_basket_item = OrderItem(basket=basket, product=product)
        new_basket_item.quantity = 1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# def basket_remove_all(request, pk):
#     if request.method == 'POST':
#         basket_item = get_object_or_404(OrderItem, pk=pk)
#         basket_item.delete()
#         print("request.META.get('HTTP_REFERER')", request.META.get('HTTP_REFERER'))
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#     else:
#         raise Http404


def basket_remove_all(request, pk):
    # if request.is_ajax():
    #     basket = get_basket(request.user)
    #     basket_item = get_object_or_404(OrderItem, pk=pk)
    #     basket_item.delete()
    #     items = OrderItem.objects.filter(basket=basket)
    #     content = {"basket":basket, "items":items,}
    #     result = render_to_string('basketapp/basket_inc.html', content)
    # else:
    #     print('1')
    #     return Http404
    # return JsonResponse({'result': result})

    if request.method == 'POST':
        data = request.data
        print(data)

