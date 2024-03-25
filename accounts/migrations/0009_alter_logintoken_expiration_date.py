import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_logintoken_expiration_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logintoken",
            name="expiration_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 25, 3, 43, 44, 335100, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
