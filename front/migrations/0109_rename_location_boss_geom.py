# Generated by Django 3.2.7 on 2022-08-23 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0108_auto_20220823_0529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boss',
            old_name='location',
            new_name='geom',
        ),
    ]