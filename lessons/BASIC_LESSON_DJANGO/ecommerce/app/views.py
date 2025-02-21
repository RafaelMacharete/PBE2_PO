from django.shortcuts import render
from .models import Product

def index(req):
    products = Product.objects.all().order_by('-product_price')
    return render(req, 'app/index.html', {'products' : products})
    
def product(req, id):
    product = Product.objects.get(id=id)
    return render(req, 'app/product.html', {'product': product})