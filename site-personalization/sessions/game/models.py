from django.db import models


class Player(models.Model):
    owner = models.BooleanField(default=False)


class Game(models.Model):
    members = models.ManyToManyField(Player, through='PlayerGameInfo', through_fields=('game', 'player'))
    guessed_number = models.PositiveIntegerField(default=0)


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE,)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    try_count = models.PositiveIntegerField(default=0)
    guessed = models.BooleanField(default=False)
