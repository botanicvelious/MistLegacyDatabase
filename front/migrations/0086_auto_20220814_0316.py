# Generated by Django 3.2.7 on 2022-08-14 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0085_blueflagsstep_is_fight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blueflagsstep',
            name='monster1_level',
        ),
        migrations.RemoveField(
            model_name='blueflagsstep',
            name='monster2_level',
        ),
        migrations.RemoveField(
            model_name='blueflagsstep',
            name='monster3_level',
        ),
        migrations.RemoveField(
            model_name='blueflagsstep',
            name='monster4_level',
        ),
        migrations.RemoveField(
            model_name='blueflagsstep',
            name='monster5_level',
        ),
    ]
