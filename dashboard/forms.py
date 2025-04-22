from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    # 'activity' field allows users to input their own activity value
    activity = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Activity', 'class': 'form-control'})
    )

    # 'name' field is a dropdown, dynamically populated from the database
    name = forms.ChoiceField(
        choices=[],  # Empty choices, will be filled in the constructor
        label="Project",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Project
        fields = ['name', 'activity', 'description', 'location', 'date', 'start_time', 'end_time']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control'}),
            'location': forms.Select(choices=Project.LOCATION_CHOICES, attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Fetch distinct project names from the database and populate the dropdown
        names_qs = Project.objects.order_by('name').values_list('name', 'name').distinct()
        choices = [('', 'Select a Project')] + list(names_qs)
        self.fields['name'].choices = choices

        # Override the widgets for the datetime fields to make sure they're correctly formatted
        self.fields['start_time'].widget.input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['end_time'].widget.input_formats = ['%Y-%m-%dT%H:%M']
