# Generated by Django 3.2.2 on 2021-05-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0031_rename_type_material_material_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='absorbency',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='density',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='durability',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='flexibility',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='hardness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='purity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='radiance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='rigidity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]