# Generated by Django 3.1.7 on 2021-02-20 14:52

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0021_auto_20210217_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='image',
        ),
        migrations.AddField(
            model_name='location',
            name='geom',
            field=djgeojson.fields.PointField(blank=True, null=True),
        ),
    ]
