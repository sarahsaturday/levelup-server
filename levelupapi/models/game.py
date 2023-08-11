"""Game class module"""
from django.db import models

class Game(models.Model):
    """Game model class"""
    title = models.CharField(max_length=150)
    type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name='games')
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
