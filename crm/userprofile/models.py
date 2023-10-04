from django.contrib.auth.models import User
from django.db import models
from team.models import Team

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    active_team = models.ForeignKey('team.Team', related_name='userprofiles', blank=True, null=True, on_delete=models.CASCADE)

    def get_active_team(self):
        return self.active_team