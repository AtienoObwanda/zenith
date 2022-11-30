from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from Store.models import Watch
from .cart import Cart

# def dum(request):

#     return render(request, 'Cart/dummy.html')


def cart_summary(request):
    cart = Cart(request)
    return render(request, 'Cart/cart.html', {'cart': cart})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        watch_id = int(request.POST.get('watchid'))
        watch_qty = int(request.POST.get('watchqty'))
        watch = get_object_or_404(Watch, id=watch_id)

        cart.add(watch=watch, qty=watch_qty)

        cartqty = cart.__len__()

        
        response = JsonResponse({'qty': cartqty})
        # response = JsonResponse({'test':'data'})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        watch_id = int(request.POST.get('watchid'))
        cart.delete(watch=watch_id)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        # response = JsonResponse({'Success': True})
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
        return response

def cart_update(request): # update
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        watch_id = int(request.POST.get('watchid'))
        watch_qty = int(request.POST.get('watchqty'))
        cart.update(watch=watch_id, qty=watch_qty)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        # newPrice = item.total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
        return response