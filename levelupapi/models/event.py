"""Event class module"""
from django.db import models

class Event(models.Model):
    """Event model class"""
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='events')
    location = models.CharField(max_length=150)
    date = models.DateField(auto_now=False, auto_now_add=False)
    attendees = models.ManyToManyField("Gamer", through='GamerEvent')
