from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_education, name='portfolio_education'),
]
