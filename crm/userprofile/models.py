from django.contrib.auth.models import User
from django.db import models
from team.models import Team

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    team = models.ForeignKey('team.Team', related_name='userprofile', blank=True, null=True, on_delete=models.CASCADE)