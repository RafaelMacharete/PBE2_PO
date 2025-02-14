from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.CharField(max_length=200)
    product_price = models.CharField(max_length=30) 