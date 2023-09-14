from django.urls import path

from .import views

urlpatterns = [
    path('add-lead/', views.add_lead, name='add_lead'),
]