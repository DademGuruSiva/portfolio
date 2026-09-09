from django.contrib import admin
from .models import About
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'email', 'phone', 'location', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at', 'location')