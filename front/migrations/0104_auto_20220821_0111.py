# Generated by Django 3.2.7 on 2022-08-21 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0103_auto_20220820_2318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blueflagsreward',
            options={},
        ),
        migrations.AlterModelOptions(
            name='blueflagsstep',
            options={},
        ),
        migrations.AlterModelOptions(
            name='bossweakness',
            options={},
        ),
        migrations.AlterModelOptions(
            name='companionskill',
            options={},
        ),
        migrations.AlterModelOptions(
            name='elixir',
            options={},
        ),
        migrations.AlterModelOptions(
            name='gatheringpoint',
            options={},
        ),
        migrations.AlterModelOptions(
            name='monsterweakness',
            options={},
        ),
        migrations.AlterModelOptions(
            name='somberseason',
            options={},
        ),
        migrations.AlterModelManagers(
            name='adventure',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='blueflags',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='blueflagsreward',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='blueflagsstep',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='book',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='boss',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='bossweakness',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='companion',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='companionskill',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='component',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='componenttype',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='cosmetics',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='crafting',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='daytime',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='elixir',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='equipmentslot',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='gathering',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='gatheringpoint',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='guide',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='guild',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='land',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='location',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='magicschool',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='material',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='materialtype',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='monster',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='monsterweakness',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='npc',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='plant',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='questitemlocations',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='recipe',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='region',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='reputation',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='somberseason',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='talent',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='training',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='weapon',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='blueflagsreward',
            name='component',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.component'),
        ),
        migrations.AlterField(
            model_name='blueflagsreward',
            name='flag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.blueflags'),
        ),
        migrations.AlterField(
            model_name='blueflagsreward',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.material'),
        ),
        migrations.AlterField(
            model_name='blueflagsreward',
            name='plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.plant'),
        ),
        migrations.AlterField(
            model_name='blueflagsstep',
            name='adventure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.adventure'),
        ),
        migrations.AlterField(
            model_name='blueflagsstep',
            name='flag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.blueflags'),
        ),
        migrations.AlterField(
            model_name='blueflagsstep',
            name='gathering',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.gathering'),
        ),
        migrations.AlterField(
            model_name='blueflagsstep',
            name='monster1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster1', to='front.monster'),
        ),
        migrations.AlterField(
            model_name='blueflagsstep',
            name='monster2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster2', to='front.monster'),
        ),
        migrations.AlterField(
            model_name='blueflagsstep',
            name='monster3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster3', to='front.monster'),
        ),
        migrations.AlterField(
            model_name='blueflagsstep',
            name='monster4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster4', to='front.monster'),
        ),
        migrations.AlterField(
            model_name='blueflagsstep',
            name='monster5',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster5', to='front.monster'),
        ),
        migrations.AlterField(
            model_name='blueflagsstep',
            name='weapon',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.weapon'),
        ),
        migrations.AlterField(
            model_name='book',
            name='adventure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.adventure'),
        ),
        migrations.AlterField(
            model_name='book',
            name='blueflag',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.blueflags'),
        ),
        migrations.AlterField(
            model_name='book',
            name='crafting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.crafting'),
        ),
        migrations.AlterField(
            model_name='book',
            name='gathering',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.gathering'),
        ),
        migrations.AlterField(
            model_name='book',
            name='guild',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.guild'),
        ),
        migrations.AlterField(
            model_name='book',
            name='land',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.land'),
        ),
        migrations.AlterField(
            model_name='book',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.location'),
        ),
        migrations.AlterField(
            model_name='book',
            name='npc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.npc'),
        ),
        migrations.AlterField(
            model_name='book',
            name='reputation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.reputation'),
        ),
        migrations.AlterField(
            model_name='book',
            name='weapon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.weapon'),
        ),
        migrations.AlterField(
            model_name='boss',
            name='substance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.component'),
        ),
        migrations.AlterField(
            model_name='bossweakness',
            name='boss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.boss'),
        ),
        migrations.AlterField(
            model_name='bossweakness',
            name='magic_school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.magicschool'),
        ),
        migrations.AlterField(
            model_name='companion',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.location'),
        ),
        migrations.AlterField(
            model_name='companion',
            name='weapon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.weapon'),
        ),
        migrations.AlterField(
            model_name='companionskill',
            name='adventure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.adventure'),
        ),
        migrations.AlterField(
            model_name='companionskill',
            name='companion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.companion'),
        ),
        migrations.AlterField(
            model_name='companionskill',
            name='crafting',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.crafting'),
        ),
        migrations.AlterField(
            model_name='companionskill',
            name='gathering',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.gathering'),
        ),
        migrations.AlterField(
            model_name='companionskill',
            name='land',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.land'),
        ),
        migrations.AlterField(
            model_name='component',
            name='component_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.componenttype'),
        ),
        migrations.AlterField(
            model_name='cosmetics',
            name='blueflag',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.blueflags'),
        ),
        migrations.AlterField(
            model_name='cosmetics',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.location'),
        ),
        migrations.AlterField(
            model_name='cosmetics',
            name='npc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.npc'),
        ),
        migrations.AlterField(
            model_name='gatheringpoint',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.material'),
        ),
        migrations.AlterField(
            model_name='gatheringpoint',
            name='plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.plant'),
        ),
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.region'),
        ),
        migrations.AlterField(
            model_name='material',
            name='material_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.materialtype'),
        ),
        migrations.AlterField(
            model_name='materialtype',
            name='gathering',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.gathering'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.region'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='substance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.component'),
        ),
        migrations.AlterField(
            model_name='monsterweakness',
            name='magic_school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.magicschool'),
        ),
        migrations.AlterField(
            model_name='monsterweakness',
            name='monster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.monster'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='daytime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.daytime'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.location'),
        ),
        migrations.AlterField(
            model_name='questitemlocations',
            name='flag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.blueflags'),
        ),
        migrations.AlterField(
            model_name='questitemlocations',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.location'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='blueflag',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.blueflags'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='equipment_slot',
            field=models.ForeignKey(blank=True, help_text='If not a building', null=True, on_delete=django.db.models.deletion.CASCADE, to='front.equipmentslot'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='guild',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.guild'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.location'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='npc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.npc'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='reputation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.reputation'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='weapon',
            field=models.ForeignKey(blank=True, help_text='If equipment_slot is weapon', null=True, on_delete=django.db.models.deletion.CASCADE, to='front.weapon'),
        ),
        migrations.AlterField(
            model_name='region',
            name='land',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.land'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='guild',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.guild'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.location'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='npc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.npc'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='reputation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.reputation'),
        ),
        migrations.AlterField(
            model_name='training',
            name='adventure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.adventure'),
        ),
        migrations.AlterField(
            model_name='training',
            name='daytime',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.daytime'),
        ),
        migrations.AlterField(
            model_name='training',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.location'),
        ),
    ]
