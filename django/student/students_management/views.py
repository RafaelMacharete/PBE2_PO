from django.shortcuts import render
from .models import Student
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#Get all students 
@api_view(['GET'])
def get_all_students(req):
    all_students = Student.objects.all()
    serializer = StudentSerializer(all_students, many=True)
    return Response(serializer.data)

# Get student object by ID
@api_view(['GET'])
def get_student_by_id(request, pk):
    try:
        student_by_pk = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(
            f"Error: {status.HTTP_404_NOT_FOUND} NOT FOUND", 
            status=status.HTTP_404_NOT_FOUND
            )

    serializer = StudentSerializer(student_by_pk)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_student(req):
    if req.method == 'POST':
        serializer = StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_student_info(req, pk):
    try:
        student_to_update = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student_to_update, data=req.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(req,pk):
    try:
        student_to_delete = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    student_to_delete.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def do_something(req, text):
    import pyfiglet
    field = pyfiglet.figlet_format(text)

    return Response(field, status=status.HTTP_200_OK)