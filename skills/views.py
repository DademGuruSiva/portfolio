from django.shortcuts import render

# Create your views here.
from .models import Skill

def skills_view(request):
    technical_skills = Skill.objects.filter(skill_type='technical')
    soft_skills = Skill.objects.filter(skill_type='soft')
    language_skills = Skill.objects.filter(skill_type='language')

    context = {
        'technical_skills': technical_skills,
        'soft_skills': soft_skills,
        'language_skills': language_skills,
    }

    return render(request, 'skills.html', context)