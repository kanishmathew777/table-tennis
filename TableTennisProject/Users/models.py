from django.db import models


# Create your models here.


class Group(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    total_matches = models.IntegerField(default=0, blank=True)
    number_of_matches_played = models.IntegerField(default=0, blank=True)
    won = models.IntegerField(default=0, blank=True)
    lost = models.IntegerField(default=0, blank=True)
    point_difference = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    group_image = models.ImageField(upload_to='media/', null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Player(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    credit_value = models.IntegerField(default=0)
    group_name = models.ForeignKey(Group, related_name='group', on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.email
