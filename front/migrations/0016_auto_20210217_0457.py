# Generated by Django 3.1.6 on 2021-02-17 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0015_location_quest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companion',
            name='quest',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='quest',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
