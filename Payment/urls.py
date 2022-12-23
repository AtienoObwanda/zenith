from django.urls import path

from . import views

app_name = 'Payment'


urlpatterns = [
    path('', views.CartView,  name='cart'),
    path('placed/orders/', views.order_placed, name='order_placed'),
    path('error/', views.Error.as_view(), name='error'),
]