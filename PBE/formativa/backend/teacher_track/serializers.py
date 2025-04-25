from rest_framework import serializers
from .models import Account, Subject, Classroom
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = {
            'username': self.user.username,
            'email': self.user.email,
            'role': self.user.role,
            'ni': self.user.ni,
            'subject': self.user.subject.name if self.user.subject else None,
            'profile_picture': self.user.profile_picture.url if self.user.profile_picture else None,
        }
        return data

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'ni', 'subject', 'name', 'email', 'phone', 'birth_date', 'hire_date', 'profile_picture', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'profile_picture': {'required': False}
        }

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'