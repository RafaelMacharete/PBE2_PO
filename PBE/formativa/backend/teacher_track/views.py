from .models import Account, Subject, Classroom
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import AccountSerializer, SubjectSerializer, ClassroomSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAdminUser
from django.db.models import Q
'''
Accounts API views
'''
# Login API view
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class AccountListCreateView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
class AccountRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    lookup_field = 'pk'
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdminUser()]
    
'''
Subjects API views
'''

class SubjectListCreateView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class SubjectRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    lookup_field = 'pk'
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

'''
Classrooms API views
'''
class ClassroomListCreateView(ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

class ClassroomRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'pk'
    serializer_class = ClassroomSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

'''
Owner attributions
'''
class OwnerSubjectsListView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(Q (responsible_teacher=self.request.user.pk) | Q (assistant_teacher=self.request.user.pk))

class OwnerClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(teacher=self.request.user.pk)