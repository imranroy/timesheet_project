from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'activity', 'description', 'location', 'date', 'start_time', 'end_time']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Project name'}),
            'activity': forms.TextInput(attrs={'placeholder': 'Activity'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'location': forms.Select(choices=Project.LOCATION_CHOICES),  # Assuming LOCATION_CHOICES in your model
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'})
        }
