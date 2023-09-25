from django.urls import path
from .import views

app_name = 'clients' #Adding name spaces to all the apps

urlpatterns = [
    path('', views.clients_list, name='list'),
    path('add/', views.clients_add, name='add'),
    path('<int:pk>/edit/', views.clients_edit, name='edit'),
    path('<int:pk>/delete/', views.clients_delete, name='delete'),
    path('<int:pk>/add-comment', views.clients_detail, name='add_comment'),
    path('<int:pk>/', views.clients_detail, name='detail'),
]