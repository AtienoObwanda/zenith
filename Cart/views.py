from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from Store.models import Watch
from .cart import Cart


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

        response = JsonResponse({'qty' : cartqty})
        return response
