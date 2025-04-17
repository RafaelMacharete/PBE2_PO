from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Character
from .serializers import CharacterSerializer, LoginSerializer, AccountSerializer


class CharacterPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 8
    

class CharacterListCreateApiView(ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    pagination_class = CharacterPagination
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        strength = request.data.get('strength')
        if int(strength) < 3:
            data = request.data.copy()
            data['strength'] = 4
            
            request._full_data = data
        return super().put(request, *args, **kwargs)
'''
class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['username']
        user_serializer = AccountSerializer(user)

        return Response({
            'user': user_serializer.data,
            'refresh': serializer.validated_data['refresh'],
            'access': serializer.validated_data['access']
        }, status=status.HTTP_200_OK)
'''

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer