# Generated by Django 4.1.4 on 2023-10-10 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custumer', '0005_alter_customuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 16, 22, 1, 322600, tzinfo=datetime.timezone.utc)),
        ),
    ]
