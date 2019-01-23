from django.contrib import admin
from .models import Team, Match, Set

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'group',)
    list_filter = ('group',)

    pass


class MatchAdmin(admin.ModelAdmin):
    list_filter = ('match_status',)

    pass


class SetAdmin(admin.ModelAdmin):
    list_filter = ('match__id', 'set_name')
    pass


admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Set, SetAdmin)
