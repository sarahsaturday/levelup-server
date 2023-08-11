from django.db import models
from django.contrib.auth.models import User


class Gamer(models.Model):
    """Gamer model class"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="gamer")
    bio = models.CharField(max_length=50)
