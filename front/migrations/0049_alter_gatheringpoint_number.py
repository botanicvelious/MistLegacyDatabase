# Generated by Django 3.2.7 on 2021-10-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0048_gatheringpoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatheringpoint',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
