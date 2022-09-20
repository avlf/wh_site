from django.contrib import admin

from .models import Character, Weapon,Roster


class CharacterAdmin(admin.ModelAdmin):
    '''fieldsets = [
        (None, {'fields': ['name','battlefield_role','power_rating', 'unit_composition','description','abilities','faction_keywords','keywors','weapons','profile']})
    ]'''
    list_display = (
    'name', 'description', 'battlefield_role', 'power_rating', 'unit_composition', 'wargear', 'abilities',
    'faction_keywords', 'keywors', 'weapons', 'profile')


class WeaponAdmin(admin.ModelAdmin):
    '''fieldsets = [
        (None, {'fields': ['name', 'range', 'type', 'strength', 'armor_penetration', 'damage', 'abilities']})
    ]'''
    list_display = ('name', 'range', 'type', 'strength', 'armor_penetration', 'damage', 'abilities')


class RosterAdmin(admin.ModelAdmin):
    list_display = ('character','troops','elite','fast_attack','heavy_support')

admin.site.register(Character, CharacterAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Roster,RosterAdmin)
