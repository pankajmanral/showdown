from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.

def all_product(request):
    products = Product.objects.all() 
    return render(request,'product/all_product.html',{'data':products})

def mens_product(request):
    mens = Product.objects.filter(tag="m")
    return render(request,'product/mens_product.html',{'men':mens})

def womens_product(request):
    womens = Product.objects.filter(tag="f")
    return render(request,'product/womens_product.html',{'women':womens})

def kids_product(request):
    kids = Product.objects.filter(tag="k")
    return render(request,'product/kids_product.html',{'kid':kids})

def product_detail(request,id):
    details = get_object_or_404(Product,id = id)
    suggestedProduct = Product.objects.all()
    return render(request,'product/product_details.html',{'detail':details,'data':suggestedProduct})