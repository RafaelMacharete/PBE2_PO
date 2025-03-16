from django.urls import path
from . import views
 
urlpatterns = [
    path('students/', views.get_all_students),
    path('student/<int:pk>/', views.get_student_by_id),
    path('student/create/', views.create_student),
    path('student/alter/<int:pk>', views.update_student_info),
    path('student/delete/<int:pk>', views.delete_student),
    path('do/something/<str:text>', views.do_something),
]