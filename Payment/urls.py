from django.urls import path

from . import views

app_name = 'Payment'


urlpatterns = [
    path('', views.payment_method,  name='payment_method'),
    path('placed/orders/', views.order_placed, name='order_placed'), #Success after payment
    path('error/', views.Error.as_view(), name='error'),
    path('mobile-money/m-pesa/', views.mpesa_payment_method, name='mpesaPay'),
    
]