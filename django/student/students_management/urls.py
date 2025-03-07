from django.urls import path
from . import views
 
urlpatterns = [
    path('students/', views.index),
    path('students/create/', views.create_stundent)
]