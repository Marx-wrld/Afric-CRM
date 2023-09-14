from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Lead(models.Model):
    #checking what priority this lead has
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    )

    #Making it possible to change the status of the lead
    NEW = 'new '
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    CHOICES_STATUS = (
        ('NEW', 'New'),
        ('CONTACTED', 'Contacted'),
        ('WON', 'Won'),
        ('LOST', 'Lost'),
    )

    #Creating the fields for the lead
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modifeid_at = models.DateTimeField(auto_now=True) # Everytime we save this db model it will be automatically updated

    def __str__(self):
        return self.name