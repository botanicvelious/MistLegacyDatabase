# Generated by Django 3.2.7 on 2022-08-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0087_questitemlocations'),
    ]

    operations = [
        migrations.AddField(
            model_name='questitemlocations',
            name='count',
            field=models.IntegerField(default=5),
        ),
    ]
