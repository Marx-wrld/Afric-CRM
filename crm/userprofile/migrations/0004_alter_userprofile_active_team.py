# Generated by Django 4.2.5 on 2023-10-04 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_alter_team_plan'),
        ('userprofile', '0003_rename_team_userprofile_active_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='active_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofiles', to='team.team'),
        ),
    ]
