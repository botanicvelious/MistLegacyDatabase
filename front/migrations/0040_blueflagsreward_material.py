# Generated by Django 3.2.7 on 2021-09-20 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0039_auto_20210920_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='blueflagsreward',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.material'),
        ),
    ]