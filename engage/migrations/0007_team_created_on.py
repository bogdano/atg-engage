# Generated by Django 5.0.1 on 2024-04-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0006_team_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
