# Generated by Django 3.2.7 on 2021-10-13 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djgeojson.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('front', '0047_elixir'),
    ]

    operations = [
        migrations.CreateModel(
            name='GatheringPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('geom', djgeojson.fields.PointField(blank=True, null=True)),
                ('icon', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gatheringpoint_icon', to=settings.FILER_IMAGE_MODEL)),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.material')),
                ('plant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.plant')),
            ],
        ),
    ]
