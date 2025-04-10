from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    defense = models.IntegerField()
    agility = models.IntegerField()
    abilities = models.CharField(max_length=40)

    def __str__(self):
        return self.name    