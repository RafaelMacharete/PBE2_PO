from django.urls import path 
from .views import CharacterListCreateApiView

urlpatterns = [
    path('characters/', CharacterListCreateApiView.as_view(), name='character_list_create')
]
