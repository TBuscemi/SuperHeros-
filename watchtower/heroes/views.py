# from typing_extensions import runtime
from django.shortcuts import redirect,render
from django.http import HttpResponse,HttpResponseRedirect
from.models import Heroes
from django.urls import reverse
# Create your views here.


def index(request):
    all_heroes = Heroes.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request,'heroes/index.html',context)

def detail(request, heroes_id):
    detail_hero = Heroes.objects.get(pk=heroes_id)
    context = {
        'detail_hero':detail_hero 
    }
    return render(request, 'heroes/detail.html', context)

def create(request):
    if request.method == 'POST':
        super_hero_name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_power = request.POST.get('primary_power')
        secondary_power = request.POST.get('secondary_power')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Heroes(super_hero_name = super_hero_name, 
        alter_ego = alter_ego, 
        primary_power = primary_power, 
        secondary_power = secondary_power, 
        catchphrase = catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('heroes:index'))
    else:
        return render(request, 'heroes/create.html')

def edit(request, heroes_id):
    if request.method == 'POST':
        new_hero = Heroes.objects.get(pk=heroes_id)
        new_hero.super_hero_name = request.POST.get('super_hero_name')
        new_hero.alter_ego = request.POST.get('alter_ego')
        new_hero.primary_power = request.POST.get('primary_power')
        new_hero.secondary_power = request.POST.get('secondary_power')
        new_hero.catchphrase = request.POST.get('catchphrase') 
        new_hero.save()
        return HttpResponseRedirect(reverse('heroes:index'))    
    
    edit_hero = Heroes.objects.get(pk=heroes_id)
    context = {
        'edit_hero': edit_hero
    }
    return render(request, 'heroes/edit.html', context)

def delete(request,heroes_id):
    if request.method =='POST':
        delete_hero = Heroes.objects.delete(pk=heroes_id)
        return HttpResponseRedirect(reverse('heroes:index'))
