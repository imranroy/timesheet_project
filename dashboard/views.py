from django.db.models import Count
from django.shortcuts import render, redirect
from .models import MasterProject, TimesheetEntry
from .forms import TimesheetEntryForm
from django.db.models import F, ExpressionWrapper, fields
from datetime import timedelta
from django.db.models import Sum, DurationField
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'dashboard/login.html'
@login_required
def dashboard_view(request):
    user = request.user

    # All entries by this user
    user_projects = TimesheetEntry.objects.filter(user=user)

    # Count of all projects (not distinct unless you want unique projects)
    total_projects = user_projects.count()

    # Unique days
    total_days = user_projects.values('date').distinct().count()

    # Total duration
    duration = user_projects.annotate(
        duration=ExpressionWrapper(F('end_time') - F('start_time'), output_field=DurationField())
    ).aggregate(total_duration=Sum('duration'))['total_duration'] or timedelta()

    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes = remainder // 60

    recent_projects = TimesheetEntry.objects.filter(user=user).order_by('-created_at')[:5]

    context = {
        'total_projects': total_projects,
        'total_days': total_days,
        'duration_hours': int(hours),
        'duration_minutes': int(minutes),
        'recent_projects':recent_projects
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def project_create(request):
    if request.method == 'POST':
        form = TimesheetEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user  # Set the user as the logged-in user
            entry.save()  # Save the entry
            return redirect('project_list')  # Redirect to project list page after saving
    else:
        form = TimesheetEntryForm()

    return render(request, 'dashboard/project_form.html', {'form': form})


@login_required
def project_list(request):
    # Get all timesheet entries created by the logged-in user, ordered by date
    entries = TimesheetEntry.objects.select_related('project').filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard/project_list.html', {'entries': entries})
