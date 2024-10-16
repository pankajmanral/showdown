from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=50, unique=True)
    brand_description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='brands/', null=True, blank=True)
    class Meta:
        # database table name in mysql xampp server
        db_table = 'brand'

    def __str__(self):
        return f'{self.brand_name} | {self.brand_description}'
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(default="Product Description")
    product_brand = models.ForeignKey(Brand,on_delete=models.CASCADE,default="Product Brand")
    product_price = models.DecimalField(decimal_places=2,max_digits=10)
    class Meta:
        # database table name in mysql xampp server
        db_table = 'product'

    def __str__(self):
        return f'{self.product_name} | {self.product_description} | {self.product_brand.brand_name} | {self.product_price}'
    
class FeaturedProduct(models.Model):
    delete_featuredProduct = models.ForeignKey(Product,on_delete=models.CASCADE)
    featured_product_name = models.CharField(max_length=100)
    featured_product_description = models.TextField(default="Product Description")
    featured_product_brand = models.ForeignKey(Brand,on_delete=models.CASCADE,default="Product Brand")
    featured_product_price = models.DecimalField(decimal_places=2,max_digits=10)
    class Meta:
        # database table name in mysql xampp server
        db_table = 'featuredProduct'

    def __str__(self):
        return f'{self.featured_product_name} | {self.featured_product_description} | {self.featured_product_brand.brand_name} | {self.featured_product_price}'