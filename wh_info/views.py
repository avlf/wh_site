from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView, CreateView, UpdateView

from .models import Character, Weapon, Roster, Strategems, Rule, Deployment_Map, Mission


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


class CreateCharacterView(CreateView):
    model = Character
    template_name = 'wh_info/create_character.html'
    fields = ('name', 'description', 'battlefield_role', 'power_rating', 'unit_composition', 'power_rating', 'cost',
        'movement', 'weapon_skill',
        'ballistic_skill', 'streath', 'tenesity', 'wd', 'leader', 'attack', 'spas_roll', 'wargear', 'abilities',
        'faction_keywords', 'weapons', 'profile')

    """def get_absolute_url(self):
        return reverse_lazy(IndexView1)"""



class UpdateCharacterView(UpdateView):
    model = Character
    template_name = 'wh_info/update_character.html'
    # context_object_name = 'character'
    fields = ('name', 'description', 'battlefield_role', 'power_rating', 'unit_composition', 'power_rating', 'cost',
        'movement', 'weapon_skill',
        'ballistic_skill', 'streath', 'tenesity', 'wd', 'leader', 'attack', 'spas_roll', 'wargear', 'abilities',
        'faction_keywords', 'weapons', 'profile')

    """def get_absolute_url(self):
        return reverse_lazy(IndexView1)"""


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


class StrategemView(DetailView):
    model = Strategems
    template_name = 'wh_info/strategems.html'
    context_object_name = 'strategems'


class StrategemALLView(generic.ListView):
    model = Strategems
    template_name = 'wh_info/all_strategems.html'
    context_object_name = 'strategems_list'


'''------------------------------------------------------------------------------------------------------------'''


class RuleView(DetailView):
    model = Rule
    template_name = 'wh_info/rule.html'
    context_object_name = 'rule'


class DeploymentMapView(DetailView):
    model = Deployment_Map
    template_name = 'wh_info/deployment_map.html'
    context_object_name = 'deployment_map'


class MissionView(DetailView):
    model = Mission
    template_name = 'wh_info/mission.html'
    context_object_name = 'mission'
