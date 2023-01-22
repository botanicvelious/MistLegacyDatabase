# Generated by Django 3.2.7 on 2022-08-18 04:59

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0090_questitemlocations_icon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questitemlocations',
            options={'ordering': ['flag']},
        ),
        migrations.AlterField(
            model_name='questitemlocations',
            name='geom',
            field=djgeojson.fields.MultiPointField(blank=True, null=True),
        ),
    ]