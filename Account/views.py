from django.shortcuts import render, redirect

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# from orders.views import user_orders

from .models import UserBase

from .forms import RegistrationForm, UserLoginForm, PwdResetForm, PwdResetConfirmForm, UserEditForm
from .token import account_activation_token


def account_register(reuest):
    if request.user.is_authenticated():
        return redirect('/')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(reuest)
            subject = 'Activate Your Account'
            message = render_to_string('account/account_activation_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('User registered successfully! Kindly check email for activation link!') # Create a page for this
        else:
            registerForm = RegistrationForm()
        return render(request, 'account/register.html', {'form': registerForm})

# def login(request):
#     return render(request, 'Account/login.html')