from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_book_form/', views.create_book, name='create_book'),   
    path('edit_book/<int:pk>', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>', views.delete_book, name='delete_book'),
    path('search_book', views.search_user, name='search_user'),
]
