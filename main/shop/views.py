from django.shortcuts import render,get_object_or_404
from product.models import Product
from account.models import Customer

def index(request):
    product = Product.objects.filter(featured_product = True)
    return render(request,'index.html',{'data':product})