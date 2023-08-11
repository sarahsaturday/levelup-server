"""GamerEvent class module"""
from django.db import models

class GamerEvent(models.Model):
    """GamerEvent intermediary model"""
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
