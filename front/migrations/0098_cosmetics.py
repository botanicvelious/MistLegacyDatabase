# Generated by Django 3.2.7 on 2022-08-20 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0097_questitemlocations_itemname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cosmetics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=1)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('reputation_guild_value', models.IntegerField(blank=True, default=0, null=True)),
                ('adventure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.adventure')),
                ('blueflag', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.blueflags')),
                ('crafting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.crafting')),
                ('gathering', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.gathering')),
                ('guild', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.guild')),
                ('land', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.land')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.location')),
                ('npc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.npc')),
                ('reputation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.reputation')),
                ('weapon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.weapon')),
            ],
            options={
                'ordering': ['gathering', 'adventure', 'crafting', 'land', 'weapon'],
            },
        ),
    ]
