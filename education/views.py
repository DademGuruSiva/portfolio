from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Education


def portfolio_education(request):
    educations = Education.objects.all().order_by('-year_of_passing')
    return render(request, 'education.html', {
        'educations': educations
    })