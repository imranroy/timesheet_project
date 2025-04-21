from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from datetime import timedelta

def dashboard_view(request):
    projects = Project.objects.all().order_by('-created_at')  # Fetch all projects, newest first

    total_projects = projects.count()
    total_days = 0
    for project in projects:
        if project.start_time and project.end_time:
            # Manually calculate duration (assuming start_time and end_time are in datetime format)
            duration = (project.end_time - project.start_time).total_seconds()  # Duration in seconds
            total_days += duration
    
    recent_projects = projects[:5]  # Take only the 5 most recent projects

    context = {
        'projects': projects,
        'total_projects': total_projects,
        'total_days': total_days,  # Duration in seconds
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
            form.save()
            return redirect('project_list')  # Redirect to project list page after saving
    else:
        form = ProjectForm()  # Initialize an empty form

    return render(request, 'dashboard/project_form.html', {'form': form})
