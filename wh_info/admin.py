from django.contrib import admin

from .models import Character, Weapon


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


'''class RosterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['stats']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('group', 'pub_date', 'was_published_recently')'''

admin.site.register(Character, CharacterAdmin)
admin.site.register(Weapon, WeaponAdmin)

# admin.site.register(Roster,RosterAdmin)
