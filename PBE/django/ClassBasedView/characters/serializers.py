from rest_framework import serializers
from .models import Character, Account
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
        read_only_fields = ['id']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
        
            if not user:
                message = "Credentials not identified"
                raise serializers.ValidationError(message, code='authorization')
            
            if not user.is_active:
                message = 'Account disabled'
                raise serializers.ValidationError(message, code='authorization')

            refresh = RefreshToken.for_user(user)

            attrs['username'] = user
            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)

            return attrs
        else:
            message = 'Username or password invalids'
            raise serializers.ValidationError(message, code='authorization')