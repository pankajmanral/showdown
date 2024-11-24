from django.shortcuts import render,redirect,get_object_or_404
from cart.models import Cart
from django.views import View
from account.forms import AddressForm
from account.models import Address,Customer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
class Checkout(View):
    def get(self,request):
        user = request.user
        user = get_object_or_404(User,username = user)
        customer = get_object_or_404(Customer,user=user)
        customerAddress = Address.objects.filter(user = customer)
        cartProduct = Cart.objects.filter(user = user)
        cart_item = cartProduct.count()
        addressForm = AddressForm()
        return render(request,'checkout/checkout.html',{'address':addressForm,'data':cartProduct,'displayAddress':customerAddress,'cartCount':cart_item})
    
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
                pincode = addressForm.cleaned_data['pincode']
            )
            
            address.save()

            # change the redirect 
            return redirect('profile')

@login_required
def select_address(request,id):
    selected_address = get_object_or_404(Address,id=id,user=request.user.customer)
    print(id)
    Address.objects.filter(user=request.user.customer, is_selected=True).update(is_selected=False)

    # Set the selected address to is_selected=True
    selected_address.is_selected = True
    selected_address.save()

    # Print the selected address (for debugging purposes)
    return redirect('checkout')