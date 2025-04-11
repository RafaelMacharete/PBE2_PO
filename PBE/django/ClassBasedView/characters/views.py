from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from .models import Character
from .serializers import CharacterSerializer


class CharacterPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 8
    

class CharacterListCreateApiView(ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    pagination_class = CharacterPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
    def perform_create(self, serializer):
        if serializer.validated_data['strength'] < 0:
            raise serializers.ValidationError('Strength must be positive')
        serializer.save()

class CharacterRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = 'pk'
    def put(self, request, *args, **kwargs):
        strength = request.data.get('strength')
        if int(strength) < 3:
            data = request.data.copy()
            data['strength'] = 4
            
            request._full_data = data
        return super().put(request, *args, **kwargs)