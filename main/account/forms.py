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
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Address Title','class':'h-12 w-80 rounded-md'}),
            'block_number': forms.TextInput(attrs={'placeholder': 'Block Number','class':'h-12 w-80 rounded-md'}),
            'building': forms.TextInput(attrs={'placeholder': 'Building Name','class':'h-12 w-80 rounded-md'}),
            'street': forms.TextInput(attrs={'placeholder': 'Street','class':'h-12 w-80 rounded-md'}),
            'land_mark': forms.TextInput(attrs={'placeholder': 'Landmark','class':'h-12 w-80 rounded-md'}),
            'area': forms.TextInput(attrs={'placeholder': 'Area','class':'h-12 w-80 rounded-md'}),
            'city': forms.TextInput(attrs={'placeholder': 'City','class':'h-12 w-80 rounded-md'}),
            'pincode': forms.TextInput(attrs={'placeholder': 'Postal Code','class':'h-12 w-80 rounded-md'}),
            'state': forms.Select(attrs={'placeholder': 'State','class':'h-12 w-full rounded-md'}),
        }
        
class ForgetPasswordForm(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter username','class':'h-12 w-60 sm:w-80 rounded-md'}))
    email = forms.CharField(max_length=50,widget=forms.EmailInput(attrs={'placeholder':'Enter email','class':'h-12 w-60 sm:w-80 rounded-md'}))

class OTPForm(forms.Form):
    otp = forms.IntegerField(max_value=9999,min_value=1000,widget=forms.NumberInput(attrs={'placeholder':'Enter 4-digit otp','class':'w-60 sm:w-80 rounded-md'}))

class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'w-60 sm:w-80 rounded-md'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'w-60 sm:w-80 rounded-md'}))
