from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='images/', null=True)
    product_price = models.CharField(max_length=30)
    product_detail = models.TextField(default='Product')

    def __str__(self):
        return self.product_name    