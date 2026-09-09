from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ('project_title', 'created_at')

    search_fields = ('project_title',)

    ordering = ('-created_at',)

   
    filter_horizontal = ('technologies',)

   
    fieldsets = (
        ('Project Info', {
            'fields': ('project_title', 'description')
        }),
        ('Technologies Used', {
            'fields': ('technologies',)
        }),
        ('Media & Link', {
            'fields': ('project_image', 'project_link')
        }),
    )