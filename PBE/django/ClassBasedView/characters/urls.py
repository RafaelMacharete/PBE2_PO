from django.urls import path 
from .views import CharacterListCreateApiView, CharacterRetrieveUpdateDestroyAPIView, LoginView

urlpatterns = [
    path('characters/', CharacterListCreateApiView.as_view(), name='character_list_create'),
    path('characters/<int:pk>', CharacterRetrieveUpdateDestroyAPIView.as_view(), name='character_retrieve_update_destroy'),
    path('login/', LoginView.as_view(), name='sigin')
]
