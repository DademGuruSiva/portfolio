from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    
    list_display = ('skill_name', 'skill_type', 'rating', 'created_at')

   
    list_filter = ('skill_type', 'rating')

    
    search_fields = ('skill_name',)


    ordering = ('-created_at',)

    
    list_editable = ('rating',)

    
    fieldsets = (
        ('Basic Information', {
            'fields': ('skill_name', 'skill_type', 'rating')
        }),
        ('Additional Details', {
            'fields': ('description', 'skill_image', 'certification')
        }),
    )