
from django.urls import path

from . import views

app_name = 'Account'


urlpatterns = [
    path('login/', views.login, name='login'),
]
