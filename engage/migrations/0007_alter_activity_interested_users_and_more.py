# Generated by Django 5.0.1 on 2024-03-04 01:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0006_activity_interested_users_delete_userinterested'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='interested_users',
            field=models.ManyToManyField(blank=True, related_name='interested_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='leaderboards',
            field=models.ManyToManyField(blank=True, related_name='leaderboards', to='engage.leaderboard'),
        ),
    ]
