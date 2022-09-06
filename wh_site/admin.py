from django.contrib import admin

from .model import List,Roster

class ListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['stats']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('stats', 'pub_date', 'was_published_recently')

class RosterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['stats']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('group', 'pub_date', 'was_published_recently')

admin.site.register(List,ListAdmin)

admin.site.register(Roster,RosterAdmin)