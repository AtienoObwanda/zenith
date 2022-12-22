import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


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


    
    
# def account_register(request):
#     if request.user.is_authenticated:
#         return redirect('Account:dashboard')
        
#     if request.method == 'POST':
#         registerForm = RegistrationForm(request.POST)
#         if registerForm.is_valid():
#             user = registerForm.save(commit=False)
#             user.email = registerForm.cleaned_data['email']
#             user.set_password(registerForm.cleaned_data['password'])
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
            # subject = 'Activate your Account'
            # message = render_to_string('Account/account_activation_email.html',{
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            #      })
            # user.email_user(subject=subject, message=message)
            
            # uName = registerForm.cleaned_data['user_name']
            # user_email = user.email
            # message = Mail(
            #     from_email='communications.weconnect@gmail.com',
            #     to_emails=[user_email],
            #     subject='Welcome To Zenith!',
            #     html_content='Hey, Your Zenith user Account has been created successfully...'
            #     )
            # print(user_email)
            # message.dynamic_template_data = {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            #     # 'user_name': uName,

            #         }
            # message.template_id =  'd-1f61c397b2334ce5b4628a9cbf19c437'
    #         user.save()
    #         try:
    #             sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    #             response = sg.send(message)
    #             print(response.status_code)
    #             print(response.body)
    #             print(response.headers)
    #         except Exception as e:
    #             print(e.message)
    #         return HttpResponse('User registered successfully! Kindly check email for activation link!') # Create a page for this
        
    # else:
    #     registerForm = RegistrationForm()
    # return render(request, 'Account/register.html', {'form': registerForm})


def account_register(request):
    if request.user.is_authenticated:
        return redirect('Account:dashboard')
        
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('Account/account_activation_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                 })
            # user.email_user(subject=subject, message=message,html_message=message)
            user.email_user(subject=subject, message=message)
            return HttpResponse('User registered successfully! Kindly check email for activation link!') # Create a page for this
        
    else:
        registerForm = RegistrationForm()
    return render(request, 'Account/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('Account:dashboard')
    else:
        return render(request, 'Account/activation_invalid.html')


@login_required
def dashboard(request):
    return render(request, 'Account/dashboard.html', {'section': 'profile'})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        
    return render(request, 'Account/edit_profile.html', {'user_form': user_form})

@login_required
def delete_user(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('Account:delete_confirmation')



# sendgrid Test config
# message = Mail(
#     from_email='communications.weconnect@gmail.com',
#     to_emails='atienoobwanda@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>'
#     )
# try:
#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
        
# except Exception as e:
#     # print(e.message)
#     print('Error!')
