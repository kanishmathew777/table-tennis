from django.contrib import admin
from .models import Team, Match, Set
from .models import Player

from django.contrib import admin


class SetInline(admin.TabularInline):
    model = Set
    fields = ('team1_score', 'team2_score', 'set_name')
    max_num = 3
    extra = 0
    verbose_name_plural = 'Match Sets'
    can_delete = False

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'group',)
    list_filter = ('group',)

    pass


class MatchAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'team_1___players', 'team_2___players', 'sets')
    list_filter = ('match_status', 'match_type')

    def team_1___players(self, obj):
        team_players = Player.objects.filter(player__id=obj.team1.id)

        return [players.name for players in team_players]

    def team_2___players(self, obj):
        team_players = Player.objects.filter(player__id=obj.team2.id)

        return [players.name for players in team_players]

    def sets(self, obj):
        sets = Set.objects.filter(match__id=obj.id)

        return ['{}-{}'.format(set.team1_score, set.team2_score) for set in sets]

    inlines = [SetInline]

    pass


class SetAdmin(admin.ModelAdmin):
    list_filter = ('match__id', 'set_name')
    pass


admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Set, SetAdmin)
