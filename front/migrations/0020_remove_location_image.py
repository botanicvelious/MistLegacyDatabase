# Generated by Django 3.1.6 on 2021-02-17 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0019_auto_20210217_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='image',
        ),
    ]
