import json

# import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from django_daraja.mpesa.core import MpesaClient

# from Orders.views import payment_confirmation
from Cart.cart import Cart


def order_placed(request):
    cart = Cart(request)
    # cart.clear()
    return render(request, 'Payment/orderPlaced.html')

class Error(TemplateView):
    template_name = 'Payment/errors.html'
    

@login_required
def CartView(request):
    cart = Cart(request)
    total = str(cart.get_total_price())
    total = total.replace('.', '')
    total = int(total)
    
    
    return render(request, 'Payment/payment.html')

@login_required
def payment_method(request):
    cart = Cart(request)
    total = str(cart.get_total_price())
    total = total.replace('.', '')
    total = int(total)
    
    return render(request, 'Payment/payment_method.html', {'total': total, cart: cart})

@login_required
def mpesa_payment_method(request):
    cl = MpesaClient()
    phone_number = '0700851861'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return render(request, 'Payment/mpesa_payment.html')