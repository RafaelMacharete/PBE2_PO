from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.create_user, name='create_user'),
    path('edit/<int:pk>', views.update_user, name='update_user'),
    path('delete/<int:pk>', views.delete_user, name='delete_user'),
]
