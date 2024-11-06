from django.urls import path
from . import views

urlpatterns = [

    path('user/',views.UserProfile.as_view(),name='profile')

]