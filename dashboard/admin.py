from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'activity', 'location', 'date', 'start_time', 'end_time']
    list_filter = ['activity', 'location', 'date']
    search_fields = ['name', 'activity']
    
    # Specify the fieldsets if needed for better organization in the admin form
    fieldsets = (
        (None, {
            'fields': ('name', 'activity', 'description', 'location', 'date', 'start_time', 'end_time')
        }),
    )

admin.site.register(Project, ProjectAdmin)
