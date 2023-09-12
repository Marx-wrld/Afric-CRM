from django.contrib import admin
from django.urls import path
from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),
]
