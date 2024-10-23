from django.db import models
from product.models import Product
from django.contrib.auth.models import User
# FeaturedProduct

# Create your models here.

class Cart(models.Model):
    cart_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'

    def __str__(self):
        return f'{self.cart_product.product_name} | {self.quantity}'
    
    def total_cost(self):
        return self.cart_product.product_price * self.quantity
        
    
# class FeaturedCart(models.Model):
#     cart_product = models.ForeignKey(FeaturedProduct,on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'FeaturedCart'
