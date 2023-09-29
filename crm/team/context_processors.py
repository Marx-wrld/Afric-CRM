from .models import Team

def team(request):
    if request.user.is_authenticated:
        return {
            'team': Team.objects.filter(members=request.user)[0]
        }
    else:
        team = None

    return {
        'team': Team.objects.all()
    }