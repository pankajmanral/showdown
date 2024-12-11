from django.db import models
from autoslug import AutoSlugField

# Create your models here.

# model to create a new brand 
class Brand(models.Model):
    brand_name = models.CharField(max_length=50, unique=True)
    brand_description = models.TextField(null=True, blank=True)

    class Meta:
        # database table name in mysql xampp server
        db_table = 'brand'

    def __str__(self):
        return f'{self.brand_name}'
                  # this thing is displayed in the admin pannel to the admin 


# model to add, delete, update new products 
# if any brand is deleted all the product of the brand will be deleted 

tag_choices = (('M',"Men"),
               ('F',"Female"),
               ('K',"Kids"))

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_slug = AutoSlugField(populate_from='product_name',blank=True,unique=True)
    product_description = models.TextField(default="Product Description")
    product_brand = models.ForeignKey(Brand,on_delete=models.CASCADE,default="Product Brand")
    product_price = models.DecimalField(decimal_places=2,max_digits=10)
    tag = models.CharField(choices=tag_choices,default=None,max_length=1)
    product_image = models.ImageField(upload_to='product/',default=r'\product\shirt.jpg')
    featured_product = models.BooleanField(default=False)

    class Meta:
        # database table name in mysql xampp server
        db_table = 'product'

    def __str__(self):
        return f'ID-{self.id} | {self.product_name} | {self.product_brand.brand_name} | {self.tag} | {self.featured_product}'
                  # this thing is displayed in the admin pannel to the admin 


# model to add some featured product on the home screen 
# if the product is deleted the featured product also get automatically deleted 

# class FeaturedProduct(models.Model):

#     featured_product = models.ForeignKey(Product,on_delete=models.CASCADE)

#     def __str__(self):
#         return f'ID : {self.id} | {self.featured_product.product_name} | {self.featured_product.tag}'
#                 # this thing is displayed in the admin pannel to the admin 

#     class Meta:
#         db_table = 'featuredProduct'