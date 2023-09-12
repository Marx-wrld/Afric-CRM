from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),
]
