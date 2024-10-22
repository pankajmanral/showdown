from django.urls import path
from . import views

urlpatterns = [

    path('cart',views.cart,name='cart'),
    path('add-to-cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('delete-product/<int:id>/',views.delete_product,name='delete_product')

]