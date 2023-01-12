from django import forms
from .models import MobilePayment

from django.core.validators import RegexValidator


# class MobileMoneyForm(forms.Form):
    # phone_number = forms.CharField(max_length=10)    
    # def clean_phone_number(self):
    #     data = self.cleaned_data['phone_number']
    #     if not re.match(r'^\d{3}-\d{3}-\d{4}$', data):
    #         raise forms.ValidationError("Invalid phone number format, should be in xxx-xxx-xxxx format")
    #     return data
    
class MobileMoneyForm(forms.ModelForm):
     class Meta:
        model = MobilePayment
        fields= ['phone_number', ]