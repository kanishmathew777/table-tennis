from .models import Match
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MATCH_CHOICES
from Users.models import Group
from django.db.models import Q


@receiver(post_save, sender=Match)
def update_group_status(sender, instance, **kwargs):
    if instance.match_status:
        groups = Group.objects.all()
        for group in groups:
            print(group.name)
            matches_completed = Match.objects.filter(Q(match_status=1),
                                                     Q(winner__isnull=False),
                                                     Q(team1__group=group) | Q(team2__group=group))

            matches_played = matches_completed.count()
            matches_won = 0
            for match in matches_completed:
                if match.winner.group == group:
                    matches_won += 1

            matches_lost = matches_played - matches_won
            total_points = matches_won * 2

            group.number_of_matches_played = matches_played
            group.won = matches_won
            group.lost = matches_lost
            group.points = total_points
            group.save()

            print(matches_played, matches_won, matches_lost, total_points)
