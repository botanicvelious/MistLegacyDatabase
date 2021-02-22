# Generated by Django 3.1.7 on 2021-02-21 12:40

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('front', '0022_auto_20210220_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='icon',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logo_icon', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='location',
            name='style',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logo_style', to=settings.FILER_IMAGE_MODEL),
        ),
    ]