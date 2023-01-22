# Generated by Django 3.2.7 on 2022-08-20 03:31

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('front', '0098_cosmetics'),
    ]

    operations = [
        migrations.AddField(
            model_name='cosmetics',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cosmetic_image', to=settings.FILER_IMAGE_MODEL),
        ),
    ]