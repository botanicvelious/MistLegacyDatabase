# Generated by Django 3.2.7 on 2021-10-24 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0052_auto_20211023_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='npc',
        ),
        migrations.AddField(
            model_name='training',
            name='daytime',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.daytime'),
        ),
    ]
