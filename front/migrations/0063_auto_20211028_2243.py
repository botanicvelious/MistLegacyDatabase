# Generated by Django 3.2.7 on 2021-10-28 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0062_auto_20211028_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blueflags',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='blueflags',
            name='name_fr',
        ),
    ]
