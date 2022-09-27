from django.contrib import admin

from .models import Character, Weapon, Roster


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'battlefield_role', 'power_rating', 'unit_composition', 'wargear', 'abilities',
        'faction_keywords', 'keywors', 'weapons', 'profile', 'power_rating', 'cost', 'movement', 'weapon_skill',
        'ballistic_skill', 'streath', 'tenesity', 'wd', 'leader', 'attack', 'spas_roll')


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'range', 'type', 'strength', 'armor_penetration', 'damage', 'abilities')


class RosterAdmin(admin.ModelAdmin):
   ''' list_display = (
        'troops', 'elite', 'fast_attack', 'heavy_support', 'flyers', 'dedicated_transport', 'lords_of_war')'''
   pass


admin.site.register(Character, CharacterAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Roster, RosterAdmin)
