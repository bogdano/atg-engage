# Generated by Django 5.0.1 on 2024-04-27 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0005_team_monthly_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
