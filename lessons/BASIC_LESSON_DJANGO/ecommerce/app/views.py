from django.shortcuts import render
from .models import Product

def index(req):
    products = Product.objects.all().order_by('-product_price')
    return render(req, 'app/index.html', {'products' : products})
    
