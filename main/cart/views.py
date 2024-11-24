from django.shortcuts import render,get_object_or_404,redirect
from . models import Cart
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json

@login_required
def cart(request):  
    # find the user using the username from the user table 
    user = get_object_or_404(User,username = request.user)
    # filter the cart based by comparing the user 
    cartProduct = Cart.objects.filter(user = user)
    return render(request,'cart/cart.html',{'product':cartProduct})
    

from product.models import Product
from .models import Cart
from django.http import JsonResponse

@login_required
def add_to_cart(request,id):
    if request.method == "POST":

        data = json.loads(request.body)
        quantity = data.get('quantity')

        user = request.user
        user = get_object_or_404(User,username=user)
        product = get_object_or_404(Product,id=id)

        try:
            obj = Cart.objects.get(user=user,cart_product=product)
            obj.quantity += quantity
            obj.save()
        except Cart.DoesNotExist:
            if 'cart_item_count' not in request.session:
                request.session['cart_item_count'] = quantity
            request.session['cart_item_count'] += 1
            Cart.objects.create(user=user,cart_product=product,quantity=quantity)

        return JsonResponse({
            'status': 'success',
            'message': 'Product added to cart successfully.'
        })

@login_required
def add(request):
    pass

@login_required
def delete_product(request,id):
    product = get_object_or_404(Cart,id=id)
    product.delete()
    return redirect('cart')

def getDetail(request,id):
    details = get_object_or_404(Product,id = id)
    suggestedProduct = Product.objects.filter(tag=details.tag).exclude(id=id)[:4]
    return render(request,'product/product_details.html',{'detail':details,'data':suggestedProduct})

def updateCartQuantity(request,id):
    cart_item = get_object_or_404(Cart,id=id)
    print(cart_item)
    action = request.GET.get('action')

    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    cart_item.save()
    return redirect('cart')