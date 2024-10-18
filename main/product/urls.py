from django.urls import path
from . import views

urlpatterns = [

    path('products/',views.all_product,name='all_product'),
    path('mens/',views.mens_product,name='mens_product'),
    path('womens/',views.womens_product,name='womens_product'),
    path('kids/',views.kids_product,name='kids_product'),
    path('detail/<int:id>/',views.product_detail,name='product_detail'),
    path('featured-product/<int:id>/',views.featured_product_detail,name='featured_product_detail'),

]