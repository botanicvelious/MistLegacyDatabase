# Generated by Django 3.2.7 on 2021-11-20 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0077_materialtype_harvest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materialtype',
            old_name='harvest',
            new_name='gathering',
        ),
    ]