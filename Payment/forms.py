from django import forms
from django.core.validators import RegexValidator


class MobileMoneyForm(forms.Form):
    phone_number = forms.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])