# Generated by Django 5.0.1 on 2024-03-04 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0002_remove_itemvariant_item_color_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activities', to='engage.activitytype'),
        ),
    ]
