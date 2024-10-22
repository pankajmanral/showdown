from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegistrationForm,CustomerRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
# Create your views here.

class Registration(View):
    def get(self,request):
        userForm = UserRegistrationForm()
        customerForm = CustomerRegistrationForm()
        context = {
            'user' : userForm,
            'customer' : customerForm
        }
        return render(request,'account/registration.html',context)
        
    def post(self,request):
        userForm = UserRegistrationForm(request.POST)
        customerForm = CustomerRegistrationForm(request.POST)

        if userForm.is_valid() and customerForm.is_valid():
            username = userForm.cleaned_data['username']
            first_name = userForm.cleaned_data['first_name']
            last_name = userForm.cleaned_data['last_name']
            email = userForm.cleaned_data['email']
            password = userForm.cleaned_data['password']

            user = User.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password
            )

            customer = customerForm.save(commit = False)
            customer.user = user
            customer.save()
            login(request,user)
            return redirect('index')