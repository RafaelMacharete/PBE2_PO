from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    biography = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=50, blank=True, null=True)
    animal_quantity = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.username