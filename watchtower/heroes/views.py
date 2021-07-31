# from typing_extensions import runtime
from django.shortcuts import render
from django.http import HttpResponse
from.models import Heroes
# Create your views here.

def index(request):
    all_heroes = Heroes.objects.all()
    context = {
        'all_movies': all_heroes
    }
    return render(request,'heroes/index.html')


    