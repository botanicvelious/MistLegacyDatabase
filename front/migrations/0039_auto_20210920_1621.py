# Generated by Django 3.2.7 on 2021-09-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0038_blueflags_blueflagsreward_blueflagsstep'),
    ]

    operations = [
        migrations.AddField(
            model_name='blueflags',
            name='name_en',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='blueflags',
            name='name_fr',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
