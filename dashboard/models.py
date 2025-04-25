from django.db import models
from django.contrib.auth.models import User

class MasterProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completion_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TimesheetEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    LOCATION_CHOICES = [
        ('office', 'Office'),
        ('home', 'Home'),
        ('client_site', 'Client Site'),
    ]
    project = models.ForeignKey(MasterProject, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project.name} - {self.activity}"
