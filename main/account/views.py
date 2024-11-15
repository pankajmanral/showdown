from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import UserRegistrationForm,CustomerRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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
                username =  userForm.cleaned_data['username']
                email = userForm.cleaned_data['email']
                
                if User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists():
                    messages.error(request,"User already exists")
                    return redirect('login')
                else:
                    user = User.objects.create_user(
                        username = username,
                        first_name = userForm.cleaned_data['first_name'],
                        last_name = userForm.cleaned_data['last_name'],
                        email = email,
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
                        fail_silently = False,
                        html_message='''
                            <div style="text-align: center; font-family: Arial, sans-serif;">
                                <div style="max-width: 600px; margin: auto;">
                                    <h1 style="color: #333;">Welcome to ClothHand, {username}!</h1>
                                    <p style="font-size: 16px; color: #666;">
                                        Thank you for joining us! We're excited to have you as part of our community. Explore our latest collections and enjoy exclusive offers tailored just for you.
                                    </p>
                                    <p style="font-size: 14px; color: #666;">
                                        If you have any questions or need assistance, feel free to reach out to our support team.
                                    </p>
                                    <p style="font-size: 14px; color: #333; font-weight: bold;">
                                        Happy shopping,<br>
                                        The ClothHand Team
                                    </p>
                                </div>
                            </div>
                        '''.format(username=user.username)
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
                fail_silently = True,
                html_message= '''
                    <div style="text-align: center;">
                        <div>
                            <h1 style="font-size: 24px; color: #333;">Welcome to ClothHand</h1>
                            <p style="font-size: 16px; color: #666;">We are glad to have you back, {username}!</p>
                        </div>
                    </div>
                '''.format(username=user.username)
            )
            return redirect('index')
        else:
            return redirect('login')
        
def logout_user(request):
    logout(request)
    return redirect('login')

from . forms import ForgetPasswordForm,OTPForm,ResetPasswordForm
import random

class ForgotPassword(View):
    def get(self,request):
        context = {
            'form':ForgetPasswordForm()
        }
        return render(request,'account/form.html',context)
    
    def post(self,request): 
        username = request.POST.get('username')
        user = get_object_or_404(User,username = username)
        email = request.POST.get('email')

        if User.objects.filter(username = username) or User.objects.filter(email = email):
        # if email == user.email:
            otp = random.randint(1000,9999)
            # send_mail(
            #     subject = "OTP for Reset Password",
            #     message = f'{otp} this is your otp for forgot password request',
            #     from_email = settings.EMAIL_HOST_USER,
            #     recipient_list = [user.email],
            #     fail_silently = True
            # )

            print('\n\n\n\n\n',otp,'\n\n\n\n')
            request.session['otp'] = int(otp)
            request.session['username'] = username
            context = {
                'form' : OTPForm(),
                'form_action' : '/account/verify-otp/',
                'otp' : 'verify-otp'
            }
            return render(request,'account/form.html',context)
        else:
            return redirect('login')
        

def verifyOTP(request):
    if request.method == "POST":
        otp = int(request.session.get('otp'))
        username = request.session.get('username')
        form_data = int(request.POST.get('otp'))   #user entered otp 
        if otp == form_data:
            context = {
                'form' : ResetPasswordForm(),
                'form_name' : f'Enter new password for {username}',
                'form_action' : '/account/reset-password/',
                
            }
            return render(request,'account/form.html',context)
    else:
        return redirect('index')
    
def resetPassword(request):
    if request.method == "POST":
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        username = request.session.get('username')
        if password == confirm_password:
            user = get_object_or_404(User,username=username)
            user.set_password(password)
            user.save()

            send_mail(
                subject = "Password Reset Complete",
                message = 'Your password has been successfully reset. You can now login with your new password',
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [user.email],
                fail_silently = True
            )

            return redirect('login')
        else:
            context = {
                'form' : ResetPasswordForm(data = request.POST),
                'form_name' : f'Password and Confirm Password did not matched for {username}',
                'form_action' : '/account/reset-password/',
                
            }
            return render(request,'account/form.html',context)
    else:
        return redirect('index')