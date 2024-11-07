from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from . forms import UserprofileForm
from account.models import Customer,Address
from account.forms import AddressForm

# Create your views here.

class UserProfile(View):
    def get(self,request):
        user = request.user
        loggedCustomer = get_object_or_404(Customer,user=user)

        form = UserprofileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'phoneNumber': loggedCustomer.phoneNumber,
            'dob': loggedCustomer.dob
        })

        address_list = Address.objects.filter(user = loggedCustomer)

        context = {
            'form': form,
            'addressForm' : AddressForm(),
            'detail' : address_list
        }

        return render(request,'userprofile/user.html',context)

    def post(self,request):
        user = request.user
        customer = get_object_or_404(Customer,user=user)
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = customer
            address.save()
            return redirect('profile')
        else:
            return redirect('index')

# def showAddress(request):
#     user = request.user
#     customer = get_object_or_404(Customer,user=user)
#     address = Address.objects.filter(user = customer)
#     context = {
#         'detail' : address
#     }
#     return render(request,'userprofile/user.html',context)
