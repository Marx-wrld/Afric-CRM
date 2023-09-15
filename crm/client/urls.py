from django.urls import path
from .import views

urlpatterns = [
    path('', views.clients_list, name='clients_list'),
    path('add/', views.clients_add, name='clients_add'),
    path('<int:pk>/edit/', views.clients_edit, name='clients_edit'),
    path('<int:pk>/delete/', views.clients_delete, name='clients_delete'),
    path('<int:pk>/', views.clients_detail, name='clients_detail'),
]