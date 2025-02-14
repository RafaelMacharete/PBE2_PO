from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_taks, name='list_tasks'),
]
