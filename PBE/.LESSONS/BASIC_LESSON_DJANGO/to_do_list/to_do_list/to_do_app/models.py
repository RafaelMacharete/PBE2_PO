from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=40)
    task_description = models.TextField()
    task_status = models.BooleanField(default=True)

    def __str__(self):
        return self.task_name