from django.shortcuts import render,get_object_or_404
from django.views import View
from . forms import UserprofileForm
from account.models import Customer,Address

# Create your views here.

class UserProfile(View):
    def get(self,request):
        user = request.user
        loggedCustomer = get_object_or_404(Customer,user=user)
        loggedCustomerAddress = get_object_or_404(Address,user=loggedCustomer)

        form = UserprofileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'phoneNumber': loggedCustomer.phoneNumber,
            'dob': loggedCustomer.dob,
            'title': loggedCustomerAddress.title,
            'block_number': loggedCustomerAddress.block_number,
            'building': loggedCustomerAddress.building,
            'street': loggedCustomerAddress.street,
            'land_mark': loggedCustomerAddress.land_mark,
            'area': loggedCustomerAddress.area,
            'pincode': loggedCustomerAddress.pincode,
        })

        context = {
            'form': form
        }

        return render(request,'userprofile/user.html',context)

    def post(self,request):
        pass


