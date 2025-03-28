from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountSerializer


@api_view(['POST'])
def login(req):
    username = req.data.get('username')
    password = req.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Error': 'Username or Password invalid'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_accounts(req):
    all_acounts = Account.objects.all()
    all_accounts_serializer = AccountSerializer(all_acounts, many=True)
    return Response(all_accounts_serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_account(req):
    username = req.data.get('username')
    password = req.data.get('password')
    email = req.data.get('email')
    is_staff = req.data.get('staff')
    biography = req.data.get('biography')
    age = req.data.get('age')
    phone_number = req.data.get('phone_number')
    address = req.data.get('address')
    education = req.data.get('education')
    animal_quantity = req.data.get('animal_quantity')

    if not username or not password or not email:
        return Response({'Error:': 'Invalid fields'}, status=status.HTTP_400_BAD_REQUEST)

    if Account.objects.filter(username = username).exists():
        return Response({'Error:': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    if Account.objects.filter(email = email).exists():
        return Response({'Error:': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

    account = Account.objects.create_user(
        username=username,
        password=password,
        email=email,
        is_staff=is_staff,
        biography=biography,
        age=age,
        phone_number=phone_number,
        address=address,
        education=education,
        animal_quantity=animal_quantity
    )

    return Response({'User created'}, status=status.HTTP_201_CREATED)
    
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def alter_account_state(req, pk):
    try:
        account_by_pk = Account.objects.get(pk=pk)
        # PUT
        if req.method == 'PUT':
            account_serializer = AccountSerializer(account_by_pk, data=req.data)
            if account_serializer.is_valid():
                account_serializer.save()
                return Response(account_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # DELETE
        elif req.method == 'DELETE':
            account_by_pk.delete()
            return Response('Account deleted',status=status.HTTP_204_NO_CONTENT)
    except Account.DoesNotExist:
        return Response({'Error:': 'User not found'}, status=status.HTTP_404_NOT_FOUND)