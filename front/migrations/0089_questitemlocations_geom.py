# Generated by Django 3.2.7 on 2022-08-18 04:48

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0088_questitemlocations_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='questitemlocations',
            name='geom',
            field=djgeojson.fields.PointField(blank=True, null=True),
        ),
    ]