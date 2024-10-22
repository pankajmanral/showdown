from django.shortcuts import render,get_object_or_404,redirect
from . models import Cart
# Create your views here.

def cart(request):
    cartProduct = Cart.objects.all()
    return render(request,'cart/cart.html',{'product':cartProduct})
    

from product.models import Product
from .models import Cart

def add_to_cart(request,id):
    product = get_object_or_404(Product,id=id)
    cart_item, created = Cart.objects.get_or_create(cart_product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def delete_product(request,id):
    product = get_object_or_404(Cart,id=id)
    product.delete()
    return redirect('cart')
