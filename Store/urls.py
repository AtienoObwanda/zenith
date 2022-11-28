from django.urls import path

from . import views

app_name = 'Store'


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('zenith/watches/<slug:slug>', views.watch_detail, name='watch_detail'),
    path('zenith/cart', views.cart_page, name='cart_detail'),

]
