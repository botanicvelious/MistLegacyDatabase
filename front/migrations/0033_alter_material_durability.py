# Generated by Django 3.2.2 on 2021-05-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0032_auto_20210516_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='durability',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
