
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .forms import *

app_name = 'Account'


urlpatterns = [
    path('register/', views.account_register, name = 'register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),    
    path('login/', auth_views.LoginView.as_view(template_name='Account/login.html', form_class=UserLoginForm), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/customer/login/'), name='logout'),
    path('profile/edit/', views.edit_profile, name='edit_details'),
    path('profile/delete_user/', views.delete_user, name='delete_user'),
    path('profile/delete_confirm/', TemplateView.as_view(template_name="Account/delete_profile.html"), name='delete_confirmation'),

    
    # Reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="Account/password_reset_form.html", success_url='password_reset_email_confirm',
                                        email_template_name='Account/password_reset_email.html',form_class=PwdResetForm), name='pwdreset'),
    
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='Account/confirm_password_reset.html',
                            success_url='customer/password_reset_complete/', form_class=PwdResetConfirmForm), name="password_reset_confirm"),
    
    path('password_reset/password_reset_email_confirm/',TemplateView.as_view(template_name="Account/reset_status.html"), name='password_reset_done'),
    
    path('password_reset_complete/',  TemplateView.as_view(template_name="Account/reset_status.html"), name='password_reset_complete'),

]
