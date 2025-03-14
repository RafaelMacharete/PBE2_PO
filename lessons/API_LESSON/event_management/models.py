from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()
    event_date = models.DateField(auto_created=False)
    event_locate = models.CharField(max_length=50, blank=True)
    event_category = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.event_name