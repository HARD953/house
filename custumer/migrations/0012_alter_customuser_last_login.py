# Generated by Django 4.1.4 on 2023-10-12 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custumer', '0011_alter_customuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 8, 56, 2, 616695, tzinfo=datetime.timezone.utc)),
        ),
    ]