# Generated by Django 5.0.1 on 2024-04-21 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0002_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]
