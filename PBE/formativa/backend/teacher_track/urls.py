from django.urls import path
from .views import (
    AccountListCreateView,
    AccountRetrieveUpdateDestroyView,
    LoginView,
    SubjectListCreateView,
    SubjectRetrieveUpdateDestroyView,
    ClassroomListCreateView,
    ClassroomRetrieveUpdateDestroyView,
    OwnerSubjectsListView,
    OwnerClassroomListView
)

urlpatterns = [
    # Login URL
    path('login/', LoginView.as_view(), name='login'),

    # Accounts URLs
    path('accounts/', AccountListCreateView.as_view(), name='account-list-create'),
    path('accounts/<int:pk>/', AccountRetrieveUpdateDestroyView.as_view(), name='account-retrieve-update-destroy'),

    # Subjects URLs
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectRetrieveUpdateDestroyView.as_view(), name='subject-retrieve-update-destroy'),

    # Classrooms URLs
    path('classrooms/', ClassroomListCreateView.as_view(), name='classroom-list-create'),
    path('classrooms/<int:pk>/', ClassroomRetrieveUpdateDestroyView.as_view(), name='classroom-retrieve-update-destroy'),

    # Owner Data Urls
    path('accounts/subject/', OwnerSubjectsListView.as_view(), name='owner_subjects-list'),    
    path('accounts/classrooms/', OwnerClassroomListView.as_view(), name='owner-classroom-list')
    
]