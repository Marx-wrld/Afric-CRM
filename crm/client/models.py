from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Client(models.Model):

    #Creating the fields for the lead
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modifeid_at = models.DateTimeField(auto_now=True) # Everytime we save this db model it will be automatically updated

    def __str__(self):
        return self.name