from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required #to prevent unauthenticated users from accessing the dashboard
def dashboard(request):
    return render(request, 'dashboard/dashboard.html') 