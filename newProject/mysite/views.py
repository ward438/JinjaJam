from django.shortcuts import render
from .models import Person

def index(request):
    return render(request, 'newProject/home.html', context={'persons': Person.objects.all()})
