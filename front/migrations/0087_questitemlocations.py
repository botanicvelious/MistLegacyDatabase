# Generated by Django 3.2.7 on 2022-08-18 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0086_auto_20220814_0316'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestItemLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.blueflags')),
            ],
        ),
    ]