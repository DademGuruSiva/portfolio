from django.shortcuts import render

# Create your views here.
# about/views.py

from .models import About

def about_view(request):
    about_data = About.objects.order_by('-updated_at').first()
    return render(request, 'about.html', {'about': about_data})