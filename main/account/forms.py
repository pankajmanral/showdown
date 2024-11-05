from django import forms
from .models import Customer,Address
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter a password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']
        field_order = ['first_name','last_name','username','email','password','confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords doesnt match")
        
        return cleaned_data

class CustomerRegistrationForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['user']

class ForgetPasswordForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.CharField(max_length=30,widget=forms.EmailInput)

class OTPForm(forms.Form):
    otp = forms.IntegerField(max_value=9999,min_value=1000)

class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
