from .models import Team

def team(request):

    return {
        'team': Team.objects.all()
    }