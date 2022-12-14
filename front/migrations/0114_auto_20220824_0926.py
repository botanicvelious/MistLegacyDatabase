# Generated by Django 3.2.7 on 2022-08-24 09:26

import auto_prefetch
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0113_remove_location_is_boss'),
    ]

    operations = [
        migrations.AddField(
            model_name='boss',
            name='material',
            field=auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.material'),
        ),
        migrations.AddField(
            model_name='monster',
            name='drops_gold',
            field=models.BooleanField(default=False),
        ),
    ]
