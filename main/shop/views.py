from django.shortcuts import render,get_object_or_404
from product.models import Product
# from wishlist.models import Wishlist

def index(request):
    product = Product.objects.filter(featured_product = True)
    # wishlist_obj = Wishlist.objects.filter(user = request.user)
    context = {
        'data' : product,
        # 'wish' : wishlist_obj
    }
    return render(request,'index.html',context)
    # return render(request,'index.html',{'data':product})