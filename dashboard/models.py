from django.db import models
from datetime import timedelta

class Project(models.Model):
    LOCATION_CHOICES = [
        ('Warehouse', 'Warehouse'),
        ('Office', 'Office'),
        ('Remote', 'Remote'),
        ('Client Site', 'Client Site'),
    ]
    
    name = models.CharField(max_length=100)
    activity = models.CharField(max_length=255, default="General")
    description = models.TextField()
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def duration(self):
        # Calculate the duration as the difference in minutes
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return timedelta()

    def __str__(self):
        return self.name
