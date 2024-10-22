from django.shortcuts import render
from cart.models import Cart

# Create your views here.

def checkout(request):
    cartProduct = Cart.objects.all()
    return render(request,'checkout/checkout.html',{'data':cartProduct})
