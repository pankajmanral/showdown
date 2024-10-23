from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegistrationForm,CustomerRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
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
            email = userForm.cleaned_data['email']
            
            if User.objects.filter(username = username).exists() or User.objects.filter(email = email):
                messages.success(request,'User already exists, Please login')
                return redirect('login')
            
            first_name = userForm.cleaned_data['first_name']
            last_name = userForm.cleaned_data['last_name']
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
        
class Login(View):
    def get(self,request):
        return render(request,'account/login.html')
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user : 
            login(request,user)
            return redirect('index')
        else:
            return render('login')
        
def logout_user(request):
    logout(request)
    return redirect('/')