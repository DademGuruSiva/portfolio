from django.contrib import admin

# Register your models here.
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'education_type',
        'institution_name',
        'board_or_university',
        'year_of_passing',
        'percentage',
        'created_at',
    )

    list_filter = (
        'education_type',
        'year_of_passing',
        'board_or_university',
    )

    search_fields = (
        'institution_name',
        'board_or_university',
        'education_type',
    )

    ordering = ('-year_of_passing',)

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Basic Information", {
            "fields": (
                'education_type',
                'institution_name',
                'board_or_university',
                'year_of_passing',
                'percentage',
                'description',
            )
        }),
        ("Uploads", {
            "fields": (
                'marksheet',
                'institution_image',
            )
        }),
        ("Timestamps", {
            "fields": (
                'created_at',
                'updated_at',
            )
        }),
    )