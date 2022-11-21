from django.shortcuts import render
from .models import Team

# Create your views here.
def index(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/index.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def cars(request):
    return render(request, 'pages/cars.html')

def service(request):
    return render(request, 'pages/service.html')

def contact(request):
    return render(request, 'pages/contact.html')