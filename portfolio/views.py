from django.shortcuts import render
from .models import Project

# Create your views here.


def home(request):
    projects = Project.objects.all()
    params = {'projects': projects}
    return render(request, 'portfolio/home.html', params)
