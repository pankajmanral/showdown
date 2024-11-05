from django.urls import path
from . import views

urlpatterns = [

    path('registration/',views.Registration.as_view(),name='registration'),
    path('login/',views.Login.as_view(),name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('forgot-password/',views.ForgotPassword.as_view(),name='forgot_password'),
    path('verify-otp/',views.verifyOTP,name='verify_otp')

]