from django.shortcuts import render,redirect
from cart.models import Cart
from django.views import View
from account.forms import AddressForm
from account.models import Address,Customer

# Create your views here.

class Checkout(View):
    def get(self,request):
        cartProduct = Cart.objects.all()
        addressForm = AddressForm()
        return render(request,'checkout/checkout.html',{'form':addressForm,'data':cartProduct})
    
    def post(self,request):
        addressForm = AddressForm(request.POST)
        if addressForm.is_valid():

            customer = Customer.objects.get(user=request.user)

            address = Address.objects.create(
                user = customer,
                title = addressForm.cleaned_data['title'],
                block_number = addressForm.cleaned_data['block_number'],
                building = addressForm.cleaned_data['building'],
                street = addressForm.cleaned_data['street'],
                land_mark = addressForm.cleaned_data['land_mark'],
                area = addressForm.cleaned_data['area'],
                city = addressForm.cleaned_data['city'],
                state = addressForm.cleaned_data['state']
            )
            
            address.save()

            # change the redirect 
            return redirect('index')