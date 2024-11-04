from django.db import models
from product.models import Product
from django.contrib.auth.models import User
# FeaturedProduct

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    cart_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['user','cart_product']]
        db_table = 'Cart'


    def __str__(self):
        return f'{self.user} | {self.cart_product.product_name} | {self.quantity}'
    
    def total_cost(self):
        return self.cart_product.product_price * self.quantity
        
    