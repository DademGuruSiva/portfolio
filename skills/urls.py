from django.urls import path
from . import views

urlpatterns = [
    path('', views.skills_view, name='skills'),  # /skills/
]