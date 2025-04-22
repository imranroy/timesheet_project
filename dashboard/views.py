from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from datetime import timedelta

def dashboard_view(request):
    projects = Project.objects.all().order_by('-created_at')

    total_projects = projects.count()
    total_seconds = 0

    # Preparing a new list to include durations
    recent_projects = []
    for project in projects[:5]:  # only top 5
        if project.start_time and project.end_time:
            duration = project.end_time - project.start_time
            total_seconds += duration.total_seconds()

            # Attach duration (in hours) to project object
            project.duration_hours = round(duration.total_seconds() / 3600, 2)
        else:
            project.duration_hours = None  # if missing

        recent_projects.append(project)

    total_hours = total_seconds / 3600

    context = {
        'projects': projects,
        'total_projects': total_projects,
        'total_days': total_hours,  # total worked hours
        'recent_projects': recent_projects,
    }
    return render(request, 'dashboard/dashboard.html', context)

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'dashboard/project_list.html', {'projects': projects})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('project_list')  # Redirect to the project list after saving
        else:
            # If the form is not valid, return the form with errors
            return render(request, 'dashboard/project_form.html', {'form': form})
    else:
        form = ProjectForm()  # If it's a GET request, render an empty form
        return render(request, 'dashboard/project_form.html', {'form': form})
