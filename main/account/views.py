from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegistrationForm,CustomerRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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

            user = User.objects.create_user(
                username =  userForm.cleaned_data['username'],
                first_name = userForm.cleaned_data['first_name'],
                last_name = userForm.cleaned_data['last_name'],
                email = userForm.cleaned_data['email'],
                password = userForm.cleaned_data['password']
            )
            
            customer = customerForm.save(commit = False)
            customer.user = user
            customer.save()
            login(request,user)

            send_mail(
                subject = "From ClothHand",
                message = f"Welcome {user.username}",
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [user.email],
                fail_silently = False
            )
            return redirect('index')
        
        context = {
            'user' : userForm,
            'customer' : customerForm
        }

        return render(request,'account/registration.html',context)
        

class Login(View):
    def get(self,request):
        return render(request,'account/login.html')
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user : 
            login(request,user)

            send_mail(
                subject = "From ClothHand",
                message = f"Welcome back {user.username}",
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [user.email],
                fail_silently = True
            )
            return redirect('index')
        else:
            return redirect('login')
        
def logout_user(request):
    logout(request)
    return redirect('/')