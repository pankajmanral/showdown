from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from order.models import Order,OrderDetails
from account.models import Customer,Address
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def orders(request):

    user = request.user

    orders = Order.objects.filter(user = user).filter(status = 'PROCESSING').order_by('order_on').order_by('order_time')
    for order in orders:
        total_amount = sum(od.quantity * od.price for od in order.orderdetails_set.all())  # Calculate total for each order
        order.total_amount = total_amount + 100

    context = {
        'order' : orders,
    }

    return render(request,'order/order.html',context)