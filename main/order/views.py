from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from order.models import Order,OrderDetails
from account.models import Customer,Address

# Create your views here.

def orders(request):

    #get the user
    user = request.user
    user = get_object_or_404(User,username = user)  # => manral02
    customer = get_object_or_404(Customer,user = user)  # => manral02     
    order = Order.objects.filter(customer = customer)   

    orderdetail = OrderDetails.objects.filter(customer = customer)
    print('details : ',orderdetail)
    context = {
        'order' : order ,
        'orderdetail' : orderdetail
    }

    return render(request,'order/order.html',context)