from __future__ import unicode_literals
import os
import json
# import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic import View


# M-Pesa
from django_daraja.mpesa.core import MpesaClient
from django_daraja.mpesa import utils
from datetime import datetime



# from Orders.views import payment_confirmation
from Cart.cart import Cart

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'

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
    # cl = MpesaClient()
    # phone_number = '0700851861'
    # amount = 1
    # account_reference = 'reference'
    # transaction_desc = 'Description'
    # callback_url = 'https://api.darajambili.com/express-payment'
    # response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return render(request, 'Payment/mpesa_payment.html')


# Test M-Pesa config
def index(request):
    cl = MpesaClient()
    phone_number = '0743068355'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def oauth_success(request):
	r = cl.access_token()
	return JsonResponse(r, safe=False)

def stk_push_success(request):
	phone_number = os.environ['LNM_PHONE_NUMBER']
	amount = 1
	account_reference = 'ABC001'
	transaction_desc = 'STK Pushc Description'
	callback_url = stk_push_callback_url
	r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
	return JsonResponse(r.response_description, safe=False)

def stk_push_callback(request):
        data = request.body
        return HttpResponse("STK Push in Django👋")