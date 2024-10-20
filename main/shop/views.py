from django.shortcuts import render
from product.models import Product

def index(request):
    product = Product.objects.filter(featured_product = True)
    print(product)
    return render(request,'index.html',{'data':product})