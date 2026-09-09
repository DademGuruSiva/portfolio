from django.shortcuts import render

# Create your views here.


from .models import Project

def projects_view(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects.html', {'projects': projects})