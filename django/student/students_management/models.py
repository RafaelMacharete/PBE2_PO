from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=150)
    student_age = models.PositiveIntegerField()
    student_course = models.CharField(max_length=50)
    student_instituition = models.CharField(max_length=200)
    rm = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student_name} {self.rm}"