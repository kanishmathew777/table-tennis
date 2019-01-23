from rest_framework import serializers
from .models import Team, Match, Set, Player
from django.conf import settings


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ('set_name', 'team2_score', 'team1_score', 'match', 'created', 'id')
        ordering = ['set_name']

    def get_unique_together_validators(self):
        '''
        Overriding method to disable unique together checks
        '''
        return []


class MatchSerializer(serializers.ModelSerializer):
    team1 = serializers.SerializerMethodField()
    team2 = serializers.SerializerMethodField()
    group1 = serializers.SerializerMethodField()
    group2 = serializers.SerializerMethodField()
    group1_image = serializers.SerializerMethodField()
    group2_image = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = ('id', 'created', 'team1', 'team2', 'group1', 'group2',
                  'match_status', 'group1_image', 'group2_image')

    def get_team1(self, obj):
        team_players = Player.objects.filter(player__id=obj.team1.id)

        return [players.name for players in team_players]

    def get_team2(self, obj):
        team_players = Player.objects.filter(player__id=obj.team2.id)

        return [players.name for players in team_players]

    def get_group1(self, obj):
        team = Team.objects.get(id=obj.team1.id)

        return team.group.name

    def get_group2(self, obj):
        team = Team.objects.get(id=obj.team2.id)

        return team.group.name

    def get_group1_image(self, obj):
        request = self.context.get('request')
        team = Team.objects.get(id=obj.team1.id)
        if team.group.group_image:
            photo_url = team.group.group_image.url
            return '{}{}{}'.format('http://', request.get_host(), photo_url)
        return None

    def get_group2_image(self, obj):
        request = self.context.get('request')
        team = Team.objects.get(id=obj.team2.id)
        if team.group.group_image:
            photo_url = team.group.group_image.url
            return '{}{}{}'.format('http://', request.get_host(), photo_url)
        return None
