from django import forms


class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(label='M-Pesa Number', max_length=10, placeholder='254 7xx xxx xxx', required=True)