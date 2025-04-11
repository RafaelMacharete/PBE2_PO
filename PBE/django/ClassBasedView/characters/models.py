from django.db import models
from django.contrib.auth.models import AbstractUser

class Character(models.Model):
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    defense = models.IntegerField()
    agility = models.IntegerField()
    abilities = models.CharField(max_length=40)

    def __str__(self):
        return self.name    
    
class Account(AbstractUser):
    name = models.CharField(max_length=10, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_foto', null=True, blank=True)