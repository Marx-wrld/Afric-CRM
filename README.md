# Afric-CRM
Implementing a customer relationship management system using Django & tailwindcss(npm), that can help business owners track and manage relationships with customers.

### Installing the Project
```
In your terminal, run:-

- pip install django
then
- pip install virtualenv
```
Finally, to create the virtual environment for our project run:-
```
- virtualenv crmenv
```
### Creating a Team using the python shell 

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
### Installing tailwind using npm in Django

- Inside the main project terminal, run:-
```
1. npm init then
2. npm install -D tailwindcss
3. npx tailwindcss init
4. After editing the tailwind config file according to your project and adding the css directives to your main.css file in static.
5. Type this in terminal - npx tailwindcss -i ./static/main.css -o ./static/main.min.css --watch
6. Add the link file path in your index html page instead of the tailwind cdn
E.g - <link rel="stylesheet" href="{% static 'main.min.css %}">
7. Ensure you add the following in the settings.py file -
STATIC_URL = 'static/'
STATICFILES_DIRS = [
        BASE_DIR / "static"
]
```
### Layout
![2023-09-29 15_40_26-](https://github.com/Marx-wrld/Afric-CRM/assets/105711066/d680ebe4-f48e-4ccb-a01c-2cdec3766a91)

![2023-09-29 15_39_01-](https://github.com/Marx-wrld/Afric-CRM/assets/105711066/1fca42f3-8a8a-4a41-88bf-2fc56cf75a07)

![2023-09-29 15_39_26-](https://github.com/Marx-wrld/Afric-CRM/assets/105711066/6722b5bb-e945-4208-882e-2320f5485a43)

