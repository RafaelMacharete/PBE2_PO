from django.db import models
from django import forms

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=18)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return 'User' + self.name
    
    class Meta:
        verbose_name_plural = "Users"