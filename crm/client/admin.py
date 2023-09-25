from django.contrib import admin
from .models import Client, Comment

# Register your models here.
admin.site.register(Client) # This will make the model visible in the admin page
admin.site.register(Comment)