# Generated by Django 3.2.7 on 2021-10-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0043_auto_20211006_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='lightness',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
