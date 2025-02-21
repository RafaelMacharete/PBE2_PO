from django.urls import path
from . import views
from .views import product

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>', product, name='product'),
]
