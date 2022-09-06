from django.contrib import admin

from .models import Character


class CharacterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']})
    ]
    list_display = ('name', 'description')


'''class RosterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['stats']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('group', 'pub_date', 'was_published_recently')'''

admin.site.register(Character, CharacterAdmin)

# admin.site.register(Roster,RosterAdmin)
