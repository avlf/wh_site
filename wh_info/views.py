from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView

from .models import Character, Weapon, Roster


class IndexView1(generic.ListView):
    template_name = 'wh_info/index1.html'
    context_object_name = "character_list"

    def get_queryset(self):
        return Character.objects.all()


class IndexView2(generic.ListView):
    template_name = 'wh_info/index2.html'
    context_object_name = 'weapon_list'

    def get_queryset(self):
        return Weapon.objects.all()


class IndexView3(generic.ListView):
    template_name = 'wh_info/index3.html'
    context_object_name = 'roster_list'

    def get_queryset(self):
        return Roster.objects.all()


class CharacterView(DetailView):
    model = Character
    template_name = 'wh_info/character.html'
    context_object_name = 'character'


class WeaponView(DetailView):
    model = Weapon
    template_name = 'wh_info/weapon.html'
    context_object_name = 'weapon'


class RosterView(DetailView):
    model = Roster
    template_name = 'wh_info/roster.html'
    context_object_name = 'roster'


def main_view(request):
    return render(request, 'wh_info/main.html')
