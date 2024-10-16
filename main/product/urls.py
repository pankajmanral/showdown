from django.urls import path
from . import views

urlpatterns = [

    path('all-products/',views.all_product,name='all_product'),
    path('mens-products/',views.mens_product,name='mens_product'),
    path('womens-products/',views.womens_product,name='womens_product'),
    path('kids-products/',views.kids_product,name='kids_product'),
    path('product-details/<int:id>/',views.product_detail,name='product_detail'),

]