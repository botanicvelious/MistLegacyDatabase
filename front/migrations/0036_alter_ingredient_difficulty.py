# Generated by Django 3.2.2 on 2021-05-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0035_auto_20210522_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='difficulty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
