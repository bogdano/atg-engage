# Generated by Django 5.0.1 on 2024-04-10 23:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_logintoken_expiration_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logintoken",
            name="expiration_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 10, 23, 53, 27, 3651, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
