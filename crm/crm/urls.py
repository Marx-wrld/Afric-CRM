from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/clients/', include('client.urls')),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/', include('dashboard.urls')), # All urls that begin with dashboard will be handled by dashboard/urls.py
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
