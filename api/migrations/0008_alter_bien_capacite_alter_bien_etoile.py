# Generated by Django 4.1.4 on 2023-10-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_bien_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='capacite',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bien',
            name='etoile',
            field=models.FloatField(),
        ),
    ]
