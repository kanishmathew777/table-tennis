from rest_framework import serializers
from .models import Team, Match, Set, Player


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ('set_name', 'team2_score', 'team1_score', 'match', 'created', 'id')
        ordering = ['set_name']


class MatchSerializer(serializers.ModelSerializer):
    team1 = serializers.SerializerMethodField()
    team2 = serializers.SerializerMethodField()
    group1 = serializers.SerializerMethodField()
    group2 = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = ('id', 'created', 'team1', 'team2', 'group1', 'group2', 'match_status')

    def get_team1(self, obj):
        team = Team.objects.get(id=obj.team1.id)

        player_list = []
        for player in team.players.all():
            player_list.append(player.name)

        return player_list

    def get_team2(self, obj):
        team = Team.objects.get(id=obj.team2.id)

        player_list = []
        for player in team.players.all():
            player_list.append(player.name)

        return player_list

    def get_group1(self, obj):
        team = Team.objects.get(id=obj.team1.id)

        return team.group.name

    def get_group2(self, obj):
        team = Team.objects.get(id=obj.team2.id)

        return team.group.name
