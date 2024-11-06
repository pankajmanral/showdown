from django import forms
from django.contrib.auth.models import User
from account.models import Address,Customer

class UserprofileForm(forms.Form):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    username = forms.CharField(max_length=40)
    email = forms.CharField(max_length=30,widget=forms.EmailInput)
    phoneNumber = forms.CharField(max_length=10)
    dob = forms.DateField()
    title = forms.CharField(max_length=15)
    block_number = forms.CharField(max_length=5)
    building = forms.CharField(max_length=30)
    street = forms.CharField(max_length=30)
    land_mark  = forms.CharField(max_length=30)
    area = forms.CharField(max_length=30)
    pincode = forms.CharField(max_length=6)
    

