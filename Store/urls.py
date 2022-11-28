from django.urls import path

from . import views

app_name = 'Store'


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('zenith/watches/<slug:slug>', views.watch_detail, name='watch_detail'),
    path('zenith/cart', views.cart_page, name='cart_detail'),
    path('zenith/brands/<slug:slug>', views.brand_detail, name='brand_detail'),
    path('zenith/categories/<slug:slug>', views.category_detail, name='category_detail'),


]
