# Generated by Django 3.1.6 on 2021-02-17 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0017_auto_20210217_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spell',
            name='image',
        ),
    ]
