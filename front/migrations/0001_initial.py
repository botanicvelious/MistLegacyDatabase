# Generated by Django 3.1.6 on 2021-02-11 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Crafting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gathering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
                ('exploration', models.IntegerField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Reputation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
                ('adventure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.adventure')),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='front.location')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
                ('price', models.IntegerField(blank=True)),
                ('reputation_guild_value', models.IntegerField(blank=True)),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='front.location')),
                ('reputation', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='front.reputation')),
                ('type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='front.recipetype')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.region'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
                ('price', models.IntegerField(blank=True)),
                ('count', models.IntegerField(blank=True)),
                ('reputation_value', models.IntegerField(blank=True)),
                ('adventure', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='front.adventure')),
                ('crafting', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='front.crafting')),
                ('gathering', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='front.gathering')),
                ('land', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='front.land')),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='front.location')),
                ('reputation', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='front.reputation')),
                ('weapon', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='front.weapon')),
            ],
        ),
    ]
