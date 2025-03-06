from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user_form/', views.create_book, name='create_book')
]
