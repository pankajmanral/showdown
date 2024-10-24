from django import forms
from .models import Customer,Address
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserRegistrationForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','confirm_password']
        field_order = ['first_name','last_name','username','email','password','confirm_password']

class CustomerRegistrationForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['user']
        # fields = ['title','block_number','building','street','land_mark','area','city','state']