from django.urls import path
from .import views

app_name = 'clients' #replacing the functional views with the client based views

urlpatterns = [
    path('', views.clients_list, name='list'),
    path('add/', views.clients_add, name='add'),
    path('<int:pk>/edit/', views.clients_edit, name='edit'),
    path('<int:pk>/delete/', views.clients_delete, name='delete'),
    path('<int:pk>/', views.clients_detail, name='detail'),
]