# Generated by Django 3.2.7 on 2021-09-20 14:17

from django.db import migrations, models
import django.db.models.deletion
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0037_plant'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlueFlags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('geom', djgeojson.fields.PolygonField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BlueFlagsStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adventure_value', models.IntegerField()),
                ('percent', models.IntegerField(default=0)),
                ('adventure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.adventure')),
                ('flag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.blueflags')),
            ],
        ),
        migrations.CreateModel(
            name='BlueFlagsReward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('flag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.blueflags')),
            ],
        ),
    ]
