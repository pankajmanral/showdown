from django.shortcuts import render
from product.models import FeaturedProduct

def index(request):
    product = FeaturedProduct.objects.all()
    return render(request,'index.html',{'data':product})