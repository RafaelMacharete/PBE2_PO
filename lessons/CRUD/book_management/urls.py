from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user_form/', views.create_book, name='create_book'),   
    path('edit_user/<int:pk>', views.edit_book, name='edit_book'),
    path('search_user', views.search_user, name='search_user')
]
