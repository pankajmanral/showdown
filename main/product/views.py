from django.shortcuts import render,get_object_or_404,redirect
from .models import Product

# Create your views here.

def all_product(request):
    products = Product.objects.all() 
    number = Product.objects.all().count()
    return render(request,'product/all_product.html',{'data':products,'number':number})

def mens_product(request):
    mens = Product.objects.filter(tag="M")
    number = Product.objects.filter(tag="M").count()
    return render(request,'product/mens_product.html',{'men':mens,'number':number})

def womens_product(request):
    womens = Product.objects.filter(tag="F")
    number = Product.objects.filter(tag="F").count()
    return render(request,'product/womens_product.html',{'women':womens,'number':number})

def kids_product(request):
    kids = Product.objects.filter(tag="K")
    number = Product.objects.filter(tag="F").count()
    return render(request,'product/kids_product.html',{'kid':kids,'number':number})

def product_detail(request,id):
    details = get_object_or_404(Product,id = id)
    suggestedProduct = Product.objects.filter(tag=details.tag).exclude(id=id)[:4]
    return render(request,'product/product_details.html',{'detail':details,'data':suggestedProduct})