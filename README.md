# Afric-CRM
Implementing a customer relationship management system using Django, that can help business owners track and manage relationships with customers.

# Creating Team

```
>>> from team.models import Team
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(pk=1)
>>> user
<User: marx>
>>> team = Team.objects.create(name='Superteam', created_by=user)
>>> team
<Team: Team object (1)>
>>> team.name
'Superteam'
>>> team.members.add(user)
>>> team.members
>>> team.members.all()[0]
<User: marx>
>>> team.save()
```
