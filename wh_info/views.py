from django.views import generic
from django.views.generic import DetailView

from .models import Character, Weapon


class IndexView(generic.ListView):
    template_name = 'wh_info/index.html'
    context_object_name = "character_list"

    def get_queryset(self):
        return Character.objects.all()

class IndexView2(generic.ListView):
    template_name = 'wh_info/index2.html'
    context_object_name = 'weapon_list'

    def get_queryset(self):
        return Weapon.objects.all()


class CharacterView(DetailView):
    model = Character
    template_name = 'wh_info/character.html'
    context_object_name = 'character'


class WeaponView(DetailView):
    model = Weapon
    template_name = 'wh_info/weapon.html'
    context_object_name = 'weapon'

class MainView(DetailView):
    model = Weapon
    template_name = 'wh_info/main.html'
    context_object_name = 'main'




