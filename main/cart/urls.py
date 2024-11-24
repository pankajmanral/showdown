from django.urls import path
from . import views

urlpatterns = [

    path('cart/',views.cart,name='cart'),
    path('add-to-cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('add/',views.add,name='add'),
    path('delete-product/<int:id>/',views.delete_product,name='delete_product'),
    path('cartDetail/<int:id>/',views.getDetail,name='cartDetail'),
    path('updateCartQuantity/<int:id>/',views.updateCartQuantity,name='updateCartQuantity')

]