# Generated by Django 3.2.7 on 2022-08-14 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0081_alter_blueflagsreward_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='blueflagsstep',
            name='monster1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.monster'),
        ),
    ]