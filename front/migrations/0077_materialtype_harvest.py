# Generated by Django 3.2.7 on 2021-11-20 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0076_auto_20211115_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialtype',
            name='harvest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.gathering'),
        ),
    ]
