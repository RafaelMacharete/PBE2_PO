from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_events),
    path('events/', views.get_events_by_params),
]
