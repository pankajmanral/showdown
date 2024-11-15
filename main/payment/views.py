from django.shortcuts import get_object_or_404,redirect
from account.models import Customer,Address
from cart.models import Cart 
from order.models import Order
from django.conf import settings
import razorpay
from payment.models import Payment
from json import dumps
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import localtime
from django.core.mail import send_mail

# Create your views here.

def procedToPay(request):
    try:

        # print(settings.RAZORPAY_KEY_ID)
        # print(settings.RAZORPAY_KEY_SECRET)
        # fetch the current user and the user cart 
        user = request.user 
        # print('top')
        user = get_object_or_404(User,username = user)
        userCart = Cart.objects.filter(user = user)

        # get the total amount to be paid 
        amount = 0
        for items in userCart:
            amount += (items.cart_product.product_price * items.quantity)
        amount *= 100
        amount = int(amount + 10000)

        # fetch the customer and the address 
        customer = get_object_or_404(Customer, user = user)
        address = Address.objects.filter(user = customer).filter(is_selected=True)[0]

        # check if the order is already created or create a new
        order = Order.objects.filter(user = user).filter(status__icontains='CREATED').first()
        if not order:
            order = Order.objects.create(
                user = user,
                customer = customer,
                status = "CREATED",
                order_time = localtime(timezone.now()).time(),
                total = amount,
                shipping_address = address,
            )

        # create new razorpay user 
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
        # print(client) # client object created 
        data = {"amount" : amount , "currency" : "INR" , "receipt" : str(order.order_uuid)}
        # print(type(data['amount']))
        payment = client.order.create(data=data)
        # print(payment)
        
        context = {
            'RAZORPAY_KEY_ID' : settings.RAZORPAY_KEY_ID,
            'payment' : payment,
            'call_back' : '/payment/verify_payment/'
        }

        Payment.objects.create(
            user = user,
            razorpay_orderId = payment['id'],
            amount = amount,
            status = "PENDING",
            method = "RAZORPAY",
            order = order
        )
        # print('bottom')
        # data = dumps(context,indent=4)
        return JsonResponse(context)

    except Exception as e:
        print(e)
        return redirect('index')    
        
from order.models import OrderDetails
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def verifyPayment(request):
    try:

        user = request.user 
        user = get_object_or_404(User,username = user)
        customer = get_object_or_404(Customer, user = user)


        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
        # print(client) - Done

        client.utility.verify_payment_signature({
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        })
        payment_obj = Payment.objects.get(razorpay_orderId = str(request.POST.get('razorpay_order_id')))
        order = payment_obj.order
        payment_obj.razorpay_paymentId = str(request.POST.get('razorpay_payment_id'))
        payment_obj.payment_signature = str(request.POST.get('razorpay_signature'))
        payment_obj.status = "COMPLETED"
        order_obj = get_object_or_404(Order,order_uuid = order.order_uuid) 
        order_obj.status = "PROCESSING"
        order_obj.save()
        payment_obj.save()

        cart = Cart.objects.filter(user = payment_obj.user)
        print(cart)

        for item in cart:
            OrderDetails.objects.create(
                order = order,
                product = item.cart_product,
                customer = customer,
                quantity = item.quantity,
                price = item.cart_product.product_price
            )

        send_mail(
            subject = "From ClothHand",
            message = f"{user.username} your order has been confirmed.",
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [user.email],
            fail_silently = True
        )
        
        cart.delete()

        return redirect('orders')    
    except Exception as e:
        return redirect('cart')