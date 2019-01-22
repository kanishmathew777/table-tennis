from django.db import models
from Users.models import Player, Group

SET_CHOICE = (
    (1, "Set 1"),
    (2, "Set 2"),
    (3, "Set 3")
)

MATCH_CHOICES = (
    (1, "COMPLETED"),
    (2, "LIVE"),
    (3, "SCHEDULED")
)


# Create your models here.

class Team(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, blank=False, related_name='player')
    group = models.ForeignKey(Group, blank=False, related_name='team_group', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Match(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    team1 = models.ForeignKey(Team, blank=False, related_name="teamone", on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, blank=False, related_name="teamtwo", on_delete=models.CASCADE)
    match_status = models.IntegerField(choices=MATCH_CHOICES, default=1)

    def __str__(self):
        return str('Match - {}'.format(self.id))


class Set(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="match_name")
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    set_name = models.IntegerField(choices=SET_CHOICE, default=1)

    def __str__(self):
        return str('Match - {} ,  Set - {}'.format(self.match.id, self.set_name))

    class meta:
        ordering = ['set_name']
