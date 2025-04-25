import datetime
from django import forms
from .models import MasterProject, TimesheetEntry

class TimesheetEntryForm(forms.ModelForm):
    # pick existing projects at runtime
    project = forms.ModelChoiceField(
        queryset=MasterProject.objects.none(),
        empty_label="Select a Project",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # dropdown of activities
    ACTIVITY_CHOICES = [
        ('General', 'General'),
        ('Development', 'Development'),
        ('Testing', 'Testing'),
        ('Deployment', 'Deployment'),
    ]
    activity = forms.ChoiceField(
        choices=ACTIVITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'})
    )

    location = forms.ChoiceField(
        choices=TimesheetEntry.LOCATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    # form-only time fields (won’t directly map to model)
    start_time_only = forms.TimeField(
        label="Start Time",
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
    )
    end_time_only = forms.TimeField(
        label="End Time",
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
    )

    class Meta:
        model = TimesheetEntry
        # note: we exclude the model's start_time/end_time here
        fields = ['project', 'activity', 'description', 'location', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # now load projects each time
        self.fields['project'].queryset = MasterProject.objects.all()

    def save(self, commit=True):
        entry = super().save(commit=False)
        # combine date + form-only times into the model’s DateTimeFields
        entry.start_time = datetime.datetime.combine(
            self.cleaned_data['date'],
            self.cleaned_data['start_time_only']
        )
        entry.end_time = datetime.datetime.combine(
            self.cleaned_data['date'],
            self.cleaned_data['end_time_only']
        )
        if commit:
            entry.save()
        return entry
