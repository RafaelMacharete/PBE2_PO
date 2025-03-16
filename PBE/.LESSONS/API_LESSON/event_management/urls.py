from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.get_create_events_by_params),
    path('events/<int:pk>', views.alter_get_event_state),
    path('events/upcoming', views.get_upcoming_events)
]
