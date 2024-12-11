# from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
# from django.contrib.auth.models import User
# from . models import Wishlist
# from product.models import Product
# from django.contrib.auth.decorators import login_required

# # Create your views here.

# def show_wishlist(request):
#     user = request.user
#     wishlist_obj = Wishlist.objects.filter(user = user)
#     context = {
#         'wish' : wishlist_obj
#     }
#     return render(request,'wishlist/wishlist.html',context)

# @login_required
# def add_to_wishlist(request,id):
#     user = request.user
#     user_obj = get_object_or_404(User, username = user)
#     product_obj = get_object_or_404(Product, id = id)
#     obj = Wishlist.objects.get_or_create(user=user_obj, wishlist_product = product_obj)

#     return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))