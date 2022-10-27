from django.contrib import admin

from .models import Character, Weapon, Roster,Strategems,Mission,Rule,Deployment_Map


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'battlefield_role', 'power_rating', 'unit_composition', 'power_rating', 'cost',
        'movement', 'weapon_skill',
        'ballistic_skill', 'streath', 'tenesity', 'wd', 'leader', 'attack', 'spas_roll', 'wargear', 'abilities',
        'faction_keywords', 'keywors', 'weapons', 'profile')


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'range', 'type', 'strength', 'armor_penetration', 'damage', 'abilities')


class RosterAdmin(admin.ModelAdmin):
    filter_horizontal = ('commanders', 'troops', 'elites', 'fast_attacks', 'heavy_supports', 'flyers')

class StrategemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'type', 'fraction', 'disription_first', 'disription_second')

"""class MinRosterAdmin(admin.ModelAdmin):
    filter_horizontal = ('commanders','troops','elites','fast_attacks','heavy_supports','flyers')"""

'''class BattalionAdmin(admin.ModelAdmin):
    list_display = (
        'com1', 'com2', 'com3',
        'tro1', 'tro2', 'tro3', 'tro4', 'tro5', 'tro6',
        'elite1', 'elite2', 'elite3', 'elite4', 'elite5', 'elite6',
        'fast_attack1', 'fast_attack2', 'fast_attack3',
        'heavy_support1', 'heavy_support2', 'heavy_support3',
        'flyers1', 'flyers2'
    )
    list_filter = ('id',)'''

class Deployment_MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'Deployment_Zone_A', 'Deployment_Zone_b', 'len_center', 'disription')

class RuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'disription')

class MissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',  'First_rule', 'Tiem_of_code', 'condition_of_win')

admin.site.register(Character, CharacterAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Roster, RosterAdmin)
"""admin.site.register(MinRoster, MinRosterAdmin)
admin.site.register(Battalion)
"""
admin.site.register(Strategems,StrategemsAdmin)

admin.site.register(Deployment_Map,Deployment_MapAdmin)
admin.site.register(Rule,RuleAdmin)
admin.site.register(Mission,MissionAdmin)
