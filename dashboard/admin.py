from django.contrib import admin
from .models import MasterProject, TimesheetEntry

@admin.register(MasterProject)
class MasterProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'completion_date', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(TimesheetEntry)
class TimesheetEntryAdmin(admin.ModelAdmin):
    list_display = ('project', 'activity', 'location', 'date', 'start_time', 'end_time')
    search_fields = ('project__name', 'activity')
    list_filter = ('location', 'date')
