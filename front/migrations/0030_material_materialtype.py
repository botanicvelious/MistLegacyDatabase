# Generated by Django 3.2.2 on 2021-05-15 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0029_auto_20210511_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
                ('level', models.IntegerField()),
                ('density', models.IntegerField()),
                ('purity', models.IntegerField()),
                ('flexibility', models.IntegerField()),
                ('rigidity', models.IntegerField()),
                ('hardness', models.IntegerField()),
                ('radiance', models.IntegerField()),
                ('absorbency', models.IntegerField()),
                ('durability', models.IntegerField()),
                ('difficulty', models.IntegerField()),
                ('encumbrance', models.IntegerField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.materialtype')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]