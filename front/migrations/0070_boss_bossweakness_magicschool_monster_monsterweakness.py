# Generated by Django 3.2.7 on 2021-11-01 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('front', '0069_rename_ingredient_type_component_component_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
                ('lvl', models.IntegerField(blank=True, null=True)),
                ('life', models.IntegerField(blank=True, null=True)),
                ('stamina', models.IntegerField(blank=True, null=True)),
                ('attack', models.IntegerField(blank=True, null=True)),
                ('armor', models.IntegerField(blank=True, null=True)),
                ('cooldown', models.IntegerField(blank=True, null=True)),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boss_image', to=settings.FILER_IMAGE_MODEL)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.location')),
                ('substance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.component')),
            ],
        ),
        migrations.CreateModel(
            name='MagicSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=64, null=True)),
                ('lvl', models.IntegerField(blank=True, null=True)),
                ('life', models.IntegerField(blank=True, null=True)),
                ('stamina', models.IntegerField(blank=True, null=True)),
                ('attack', models.IntegerField(blank=True, null=True)),
                ('armor', models.IntegerField(blank=True, null=True)),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster_image', to=settings.FILER_IMAGE_MODEL)),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.region')),
                ('substance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.component')),
            ],
        ),
        migrations.CreateModel(
            name='MonsterWeakness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField(blank=True, null=True)),
                ('magic_school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.magicschool')),
                ('monster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.monster')),
            ],
        ),
        migrations.CreateModel(
            name='BossWeakness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField(blank=True, null=True)),
                ('boss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.boss')),
                ('magic_school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.magicschool')),
            ],
        ),
    ]
