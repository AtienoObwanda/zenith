from django.urls import path, include

from . import views

app_name = 'Payment'


test_patterns = [
    path('test-home', views.index, name='django_daraja_index'),
	path('oauth/success', views.oauth_success, name='test_oauth_success'),
	path('stk-push/success', views.stk_push_success, name='test_stk_push_success'),
]

urlpatterns = [
    path('', views.payment_method,  name='payment_method'),
    path('daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),
    path('placed/orders/', views.order_placed, name='order_placed'), #Success after payment
    path('error/', views.Error.as_view(), name='error'),
    path('mobile-money/m-pesa/', views.mpesa_payment_method, name='mpesaPay'),
    path('tests/', include(test_patterns), name='tests'),   
]