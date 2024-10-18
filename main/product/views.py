from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.

def all_product(request):
    products = Product.objects.all() 
    number = Product.objects.all().count()
    return render(request,'product/all_product.html',{'data':products,'number':number})

def mens_product(request):
    mens = Product.objects.filter(tag="m")
    number = Product.objects.filter(tag="m").count()
    return render(request,'product/mens_product.html',{'men':mens,'number':number})

def womens_product(request):
    womens = Product.objects.filter(tag="f")
    number = Product.objects.filter(tag="f").count()
    return render(request,'product/womens_product.html',{'women':womens,'number':number})

def kids_product(request):
    kids = Product.objects.filter(tag="k")
    return render(request,'product/kids_product.html',{'kid':kids})

def product_detail(request,id):
    details = get_object_or_404(Product,id = id)
    print(details)
    suggestedProduct = Product.objects.filter(tag=details.tag).exclude(id=id)[:4]
    return render(request,'product/product_details.html',{'detail':details,'data':suggestedProduct})

from .models import FeaturedProduct

def featured_product_detail(request,id):
    data = get_object_or_404(FeaturedProduct,id=id)
    suggestedProduct = Product.objects.filter(tag=data.featured_product.tag).exclude(id=data.featured_product.id)
    return render(request,'product/featured_product_detail.html',{'data':data,'suggested':suggestedProduct})