# Generated by Django 4.1.4 on 2023-10-12 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custumer', '0012_alter_customuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 9, 23, 35, 120583, tzinfo=datetime.timezone.utc)),
        ),
    ]