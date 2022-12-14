from django.urls import path

from . import views

app_name = 'Store'


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('zenith/watches/<slug:slug>', views.watch_detail, name='watch_detail'),
    path('zenith/brands/<slug:brand_slug>', views.brand_detail, name='brand_detail'),
    path('zenith/categories/<slug:category_slug>', views.category_detail, name='category_detail'),


]
