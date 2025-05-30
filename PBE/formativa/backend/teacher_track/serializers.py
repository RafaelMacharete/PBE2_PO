from rest_framework import serializers
from .models import Account, Subject, Classroom
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            'username': self.user.username,
        }
        # After successful login, you can add more user details if needed
        return data

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'subject', 'email', 'phone', 'birth_date', 'hire_date', 'profile_picture', 'password', 'name', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        # Makes sure that the password is only writable and not readable

    def create(self, validated_data):
        user = Account.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            subject=validated_data['subject'],
            email=validated_data['email'],
            birth_date=validated_data['birth_date'],
            hire_date=validated_data['hire_date'],
            phone=validated_data['phone'],
            name=validated_data['name'],
            is_staff=validated_data['is_staff']
        ) # Create a new user with the given data
        return user
    
    def update(self, instance, validated_data):
        '''
        Update an existing user instance with the provided validated data.
        This is used to save the password with the crypted hash
        and update other fields as necessary.
        '''
        
        password = validated_data.pop('password', None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        if password:
            instance.set_password(password)
            
        instance.save()
        return instance
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'