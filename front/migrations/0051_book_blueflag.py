# Generated by Django 3.2.7 on 2021-10-16 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0050_auto_20211013_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='blueflag',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.blueflags'),
        ),
    ]