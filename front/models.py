import auto_prefetch
from django.db import models
from django.urls import reverse
from djgeojson.fields import PointField, PolygonField, MultiPointField
from django.utils.translation import gettext as _
from filer.fields.image import FilerImageField
from .toolbox import centroid

WEAKNESS_CHOICES = [
    ('+', '+'),
    ('-', '-')
]

COOLDOWN_CHOICES = [
    (_('Daily'), 'Daily'),
    (_('Weekly'), 'Weekly')
]


class Daytime(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Weapon(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('weapon', args=[str(self.id)])


class EquipmentSlot(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Land(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('land', args=[str(self.id)])


class Gathering(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gathering', args=[str(self.id)])


class Adventure(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('adventure', args=[str(self.id)])


class Crafting(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crafting', args=[str(self.id)])


class Reputation(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reputation', args=[str(self.id)])


class Guild(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('guild', args=[str(self.id)])


class Region(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    land = auto_prefetch.ForeignKey(Land, on_delete=models.CASCADE, blank=True, null=True)
    land_difficulty = models.IntegerField(blank=True, null=True)
    geom = PolygonField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')

    @property
    def map_poi(self):
        tooltip = "<p>{} ({} {})".format(self.name, self.land, self.land_difficulty)
        if self.monster_set.all().exists():
            tooltip = tooltip + '</br></br>{}(s):</br>'.format(_("Monster"))
            for monster in self.monster_set.all():
                if monster.name and monster.lvl:
                    tooltip = tooltip + '{} lvl {}'.format(monster.name, monster.lvl)
                    if monster.substance:
                        tooltip = tooltip + ' ({})'.format(monster.substance.name)
                    tooltip = tooltip + '</br>'
        tooltip = tooltip + '</p>'
        return tooltip

    @property
    def coordinates(self):
        if self.geom:
            return str(centroid(self.geom)['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None


class Location(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    region = auto_prefetch.ForeignKey(Region, on_delete=models.CASCADE)
    exploration = models.IntegerField(blank=True, null=True)
    quest = models.BooleanField(blank=True, null=True, default=False)
    geom = PointField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True, related_name="location_icon", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')

    @property
    def map_poi(self):
        tooltip = "<p>{}".format(self.name)
        if self.quest:
            tooltip = tooltip + ' ({})'.format(_("Quest"))
        if self.exploration:
            tooltip = tooltip + '</br>{}({})'.format(_("Exploration"), self.exploration)
        if self.companion_set.all().exists():
            tooltip = tooltip + '</br>{}(s):</br>'.format(_("Companion"))
            for companion in self.companion_set.all():
                tooltip = tooltip + '{}</br>'.format(companion.name)
        if self.training_set.all().exists():
            tooltip = tooltip + '</br>{}(s):</br>'.format(_("Training"))
            for training in self.training_set.all():
                tooltip = tooltip + '{} ({})</br>'.format(training.adventure, training.difficulty)
        if self.book_set.all().exists():
            tooltip = tooltip + '</br>{}(s):</br>'.format(_("Book"))
            for book in self.book_set.all():
                tooltip = tooltip + '{} ({}/{})</br>'.format(book.__str__(), book.reputation, book.reputation_guild_value)
        if self.recipe_set.all().exists():
            tooltip = tooltip + '</br>{}(s):</br>'.format(_("Recipe & Item"))
            for recipe in self.recipe_set.all():
                tooltip = tooltip + '{} ({}/{})</br>'.format(recipe.name, recipe.reputation, recipe.reputation_guild_value)
        if self.talent_set.all().exists():
            tooltip = tooltip + '</br>{}(s):</br>'.format(_("Talent"))
            for spell in self.talent_set.all():
                rep = spell.reputation or spell.guild
                tooltip = tooltip + '{} ({}/{})</br>'.format(spell.name, rep, spell.reputation_guild_value)
        if self.boss_set.all().exists():
            for boss in self.boss_set.all().order_by('elite'):
                tooltip = tooltip + '</br>{}: {}({})'.format(boss.cooldown, boss.name, boss.lvl)
                if boss.substance is not None:
                    tooltip = tooltip + '- {}'.format(boss.substance)
                if boss.material is not None:
                    tooltip = tooltip + '- {}'.format(boss.material)
        tooltip = tooltip + '</p>'
        return tooltip

    @property
    def icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return None

    @property
    def icon_width(self):
        if self.icon:
            return self.icon.width
        else:
            return None

    @property
    def icon_height(self):
        if self.icon:
            return self.icon.height
        else:
            return None

    @property
    def coordinates(self):
        if self.geom:
            return str(self.geom['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None


class Companion(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    lvl = models.IntegerField(blank=True, null=True)
    location = auto_prefetch.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    quest = models.BooleanField(blank=True, null=True, default=False)
    weapon = auto_prefetch.ForeignKey(Weapon, on_delete=models.CASCADE, blank=True, null=True)
    weapon_lvl = models.IntegerField(blank=True, null=True)
    comfort = models.IntegerField(blank=True, null=True)
    convenience = models.IntegerField(blank=True, null=True)
    armor = models.IntegerField(blank=True, null=True)
    life = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class CompanionSkill(auto_prefetch.Model):
    companion = auto_prefetch.ForeignKey(Companion, null=False, blank=False, on_delete=models.CASCADE)
    adventure = auto_prefetch.ForeignKey(Adventure, null=True, blank=True, on_delete=models.CASCADE)
    gathering = auto_prefetch.ForeignKey(Gathering, null=True, blank=True, on_delete=models.CASCADE, default=None)
    land = auto_prefetch.ForeignKey(Land, null=True, blank=True, on_delete=models.CASCADE, default=None)
    crafting = auto_prefetch.ForeignKey(Crafting, null=True, blank=True, on_delete=models.CASCADE, default=None)
    bonus = models.IntegerField(null=False, blank=False)


class NPC(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    location = auto_prefetch.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    daytime = auto_prefetch.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class Recipe(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    reputation = auto_prefetch.ForeignKey(Reputation, on_delete=models.CASCADE, blank=True, null=True)
    guild = auto_prefetch.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)
    reputation_guild_value = models.IntegerField(blank=True, null=True)
    location = auto_prefetch.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    npc = auto_prefetch.ForeignKey(NPC, on_delete=models.CASCADE, blank=True, null=True)
    building = models.BooleanField(default=False)
    equipment_slot = auto_prefetch.ForeignKey(EquipmentSlot, on_delete=models.CASCADE, blank=True, null=True,
                                       help_text="If not a building")
    weapon = auto_prefetch.ForeignKey(Weapon, on_delete=models.CASCADE, blank=True, null=True,
                               help_text="If equipment_slot is weapon")
    blueflag = auto_prefetch.ForeignKey('BlueFlags', on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')

    def get_absolute_url(self):
        return reverse('recipe_card', args=[str(self.id)])

    def get_reputation(self):
        if self.reputation:
            return '{} {}'.format(self.reputation, self.reputation_guild_value)
        elif self.guild:
            return '{} {}'.format(self.guild, self.reputation_guild_value)

    def get_location(self):
        if self.location:
            return self.location
        elif self.blueflag:
            return self.blueflag
        else:
            return None


class Training(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    adventure = auto_prefetch.ForeignKey(Adventure, on_delete=models.CASCADE, blank=True, null=True)
    land = auto_prefetch.ForeignKey(Land, on_delete=models.CASCADE, blank=True, null=True)
    location = auto_prefetch.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    difficulty = models.IntegerField(blank=True, null=True)
    daytime = auto_prefetch.ForeignKey(Daytime, on_delete=models.CASCADE, blank=True, null=True, default=3)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class Talent(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    level = models.IntegerField(default=1)
    price = models.IntegerField(blank=True, null=True)
    reputation = auto_prefetch.ForeignKey(Reputation, on_delete=models.CASCADE, blank=True, null=True)
    guild = auto_prefetch.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)
    reputation_guild_value = models.IntegerField(blank=True, null=True)
    location = auto_prefetch.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    npc = auto_prefetch.ForeignKey(NPC, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')

    def get_absolute_url(self):
        return reverse('talent_card', args=[str(self.id)])

    def get_reputation(self):
        if self.reputation:
            return '{} {}'.format(self.reputation, self.reputation_guild_value)
        elif self.guild:
            return '{} {}'.format(self.guild, self.reputation_guild_value)


class MaterialType(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    gathering = auto_prefetch.ForeignKey(Gathering, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class ComponentType(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Material(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    material_type = auto_prefetch.ForeignKey(MaterialType, on_delete=models.CASCADE, blank=False, null=False)
    level = models.IntegerField(blank=False, null=False)
    density = models.IntegerField(default=0)
    purity = models.IntegerField(default=0)
    flexibility = models.IntegerField(default=0)
    rigidity = models.IntegerField(default=0)
    hardness = models.IntegerField(default=0)
    radiance = models.IntegerField(default=0)
    absorbency = models.IntegerField(default=0)
    lightness = models.IntegerField(default=0)
    durability = models.IntegerField(blank=False, null=False)
    craft_difficulty = models.IntegerField(default=0)
    harvest_difficulty = models.IntegerField(blank=True, null=True)
    cooldown = models.FloatField(blank=True, null=True)
    encumbrance = models.IntegerField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True, related_name="material_icon", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    @property
    def icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return None

    @property
    def icon_width(self):
        if self.icon:
            return self.icon.width
        else:
            return None

    @property
    def icon_height(self):
        if self.icon:
            return self.icon.height
        else:
            return None

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class Component(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    component_type = auto_prefetch.ForeignKey(ComponentType, on_delete=models.CASCADE, blank=False, null=False)
    level = models.IntegerField(blank=False, null=False)
    lithram = models.IntegerField(default=0)
    magnam = models.IntegerField(default=0)
    radiam = models.IntegerField(default=0)
    hydram = models.IntegerField(default=0)
    pyram = models.IntegerField(default=0)
    stratam = models.IntegerField(default=0)
    frimam = models.IntegerField(default=0)
    lectram = models.IntegerField(default=0)
    psycham = models.IntegerField(default=0)
    elioam = models.IntegerField(default=0)
    craft_difficulty = models.IntegerField(default=0)
    encumbrance = models.IntegerField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True, related_name="ingredient_icon", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    @property
    def icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return None

    @property
    def icon_width(self):
        if self.icon:
            return self.icon.width
        else:
            return None

    @property
    def icon_height(self):
        if self.icon:
            return self.icon.height
        else:
            return None

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class Plant(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    level = models.IntegerField(blank=False, null=False)
    activator = models.IntegerField(default=0)
    binder = models.IntegerField(default=0)
    energizer = models.IntegerField(default=0)
    deteriorator = models.IntegerField(default=0)
    focuser = models.IntegerField(default=0)
    fortifier = models.IntegerField(default=0)
    putrefier = models.IntegerField(default=0)
    stimulator = models.IntegerField(default=0)
    tranquilizer = models.IntegerField(default=0)
    toner = models.IntegerField(default=0)
    craft_difficulty = models.IntegerField(default=0)
    harvest_difficulty = models.IntegerField(blank=True, null=True)
    cooldown = models.FloatField(blank=True, null=True)
    encumbrance = models.IntegerField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True, related_name="plant_icon", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    @property
    def icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return None

    @property
    def icon_width(self):
        if self.icon:
            return self.icon.width
        else:
            return None

    @property
    def icon_height(self):
        if self.icon:
            return self.icon.height
        else:
            return None

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')


class BlueFlags(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    geom = PointField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True, related_name="blueflag_icon", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def map_poi(self):
        tooltip = "<p>{}</br>".format(self.name)
        if self.blueflagsstep_set.all().exists():
            tooltip = tooltip + '</br>{}(s):</br>'.format(_("Step"))
            for step in self.blueflagsstep_set.all():
                if step.adventure:
                    tooltip = tooltip + '{}% {} ({})</br>'.format(step.percent, step.adventure, step.difficulty)
                elif step.weapon:
                    tooltip = tooltip + '{}% {} ({})</br>'.format(step.percent, step.weapon, step.difficulty)
                elif step.gathering:
                    tooltip = tooltip + '{}% {} ({})</br>'.format(step.percent, step.gathering, step.difficulty)
                elif step.is_fight == True:
                    tooltip = tooltip + '{}% Fight: </br>'.format(step.percent, step.monster1)
                    if step.monster1: 
                        tooltip = tooltip + '{} Level: {}</br>'.format(step.monster1, Monster.objects.get(id=step.monster1.id).lvl)
                    if step.monster2:
                        tooltip = tooltip + '{} Level: {}</br>'.format(step.monster2, Monster.objects.get(id=step.monster2.id).lvl)
                    if step.monster3:
                        tooltip = tooltip + '{} Level: {}</br>'.format(step.monster3, Monster.objects.get(id=step.monster3.id).lvl)
                    if step.monster4:
                        tooltip = tooltip + '{} Level: {}</br>'.format(step.monster4, Monster.objects.get(id=step.monster4.id).lvl)
                    if step.monster5:
                        tooltip = tooltip + '{} Level: {}</br>'.format(step.monster5, Monster.objects.get(id=step.monster5.id).lvl)

        tooltip = tooltip + '</br>{}(s):</br>'.format(_("Reward"))
        rewards = self.blueflagsreward_set.all()
        if rewards is not None:
            for reward in rewards:
                if reward.number is not None:
                    tooltip = tooltip + '{} ({})</br>'.format(reward.__str__(), reward.number)
                else:
                    tooltip = tooltip + '{}</br>'.format(reward.__str__())
        books = self.book_set.all()
        if books is not None:
            for book in books:
                tooltip = tooltip + '{} {}</br>'.format(_("Book"), book.__str__())
        recipes = self.recipe_set.all()
        if recipes is not None:
            for recipe in recipes:
                tooltip = tooltip + '{} {}</br>'.format(_("Recipe"), recipe.__str__())
        tooltip = tooltip + '</p>'
        return tooltip

    @property
    def coordinates(self):
        if self.geom:
            return str(self.geom['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None

    @property
    def icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return None




class BlueFlagsReward(auto_prefetch.Model):
    flag = auto_prefetch.ForeignKey(BlueFlags, null=False, blank=False, on_delete=models.CASCADE)
    material = auto_prefetch.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    component = auto_prefetch.ForeignKey(Component, null=True, blank=True, on_delete=models.CASCADE)
    plant = auto_prefetch.ForeignKey(Plant, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=1024, blank=True)


    def __str__(self):
        if self.material and self.material.name:
            return self.material.name
        elif self.component and self.component.name:
            return self.component.name
        elif self.plant and self.plant.name:
            return self.plant.name
        elif self.notes:
            return self.notes
        else:
            return _('-- no translation yet --')


class Elixir(auto_prefetch.Model):
    geom = PointField(blank=True, null=True)

    def __str__(self):
        return _('Vigor')

    @property
    def map_poi(self):
        return self.__str__()

    @property
    def coordinates(self):
        if self.geom:
            return str(self.geom['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None


class GatheringPoint(auto_prefetch.Model):
    material = auto_prefetch.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    plant = auto_prefetch.ForeignKey(Plant, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, null=True)
    geom = PointField(blank=True, null=True)

    def __str__(self):
        if self.material:
            return self.material.name
        elif self.plant:
            return self.plant.name
        else:
            return _('-- no translation yet --')

    @property
    def map_poi(self):
        if self.material:
            tooltip = '{} x {}'.format(self.material.name, self.number)
            if self.material.material_type.gathering:
                tooltip = tooltip + ' ({} {})'.format(self.material.material_type.gathering.name, self.material.harvest_difficulty)
            if self.material.cooldown:
                tooltip = tooltip + '<br/>{} : {} {}'.format(_("Cooldown"), self.material.cooldown, _("hours"))
        elif self.plant:
            tooltip = '{} x {}'.format(self.plant.name, self.number)
            tooltip = tooltip + ' ({} {})'.format(_("Botany"), self.plant.harvest_difficulty)
            if self.plant.cooldown:
                tooltip = tooltip + '<br/>{} : {} {}'.format(_("Cooldown"), self.plant.cooldown, _("hours"))
        return tooltip

    @property
    def icon_url(self):
        if self.material and self.material.icon:
            return self.material.icon.url
        elif self.plant and self.plant.icon:
            return self.plant.icon.url
        else:
            return None

    @property
    def coordinates(self):
        if self.geom:
            return str(self.geom['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None


class Guide(auto_prefetch.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    link = models.CharField(max_length=256, blank=True, null=True)
    author = models.CharField(max_length=64, blank=True, null=True)
    contact = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        ordering = ["name"]


class Somberseason(auto_prefetch.Model):
    clue = models.CharField(max_length=64, blank=True, null=True)
    geom = PointField(blank=True, null=True)

    @property
    def map_poi(self):
        if self.clue:
            return self.clue
        else:
            return _('Always')


class MagicSchool(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Monster(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    lvl = models.IntegerField(blank=True, null=True)
    life = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    armor = models.IntegerField(blank=True, null=True)
    substance = auto_prefetch.ForeignKey(Component, blank=True, null=True, on_delete=models.CASCADE)
    region = auto_prefetch.ForeignKey(Region, blank=True, null=True, on_delete=models.CASCADE)
    image = FilerImageField(blank=True, null=True, related_name="monster_image", on_delete=models.CASCADE)
    elite = models.BooleanField(default=False)
    drops_gold = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')

    def get_region(self):
        if self.region:
            return self.region
        else:
            return None


class MonsterWeakness(auto_prefetch.Model):
    monster = auto_prefetch.ForeignKey(Monster, blank=True, null=True, on_delete=models.CASCADE)
    magic_school = auto_prefetch.ForeignKey(MagicSchool, blank=True, null=True, on_delete=models.CASCADE)
    bonus = models.CharField(max_length=1, blank=True, null=True, choices=WEAKNESS_CHOICES, default='+')
    percent = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.magic_school.name


class Boss(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    lvl = models.IntegerField(blank=True, null=True)
    life = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    armor = models.IntegerField(blank=True, null=True)
    substance = auto_prefetch.ForeignKey(Component, blank=True, null=True, on_delete=models.CASCADE)
    cooldown = models.CharField(max_length=16, blank=True, null=True, choices=COOLDOWN_CHOICES, default='Daily')
    image = FilerImageField(blank=True, null=True, related_name="boss_image", on_delete=models.CASCADE)
    elite = models.BooleanField(default=False)
    location = auto_prefetch.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    material = auto_prefetch.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        else:
            return _('-- no translation yet --')

    @property
    def map_poi(self):
        return '{} lvl {} ({})'.format(self.name, self.lvl, self.cooldown)

    @property
    def coordinates(self):
        if self.location:
            return str(self.location.geom['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None

    @property
    def geom(self):
        if self.location:
            return self.location.geom
        else:
            return None

class BossWeakness(auto_prefetch.Model):
    boss = auto_prefetch.ForeignKey(Boss, blank=True, null=True, on_delete=models.CASCADE)
    magic_school = auto_prefetch.ForeignKey(MagicSchool, blank=True, null=True, on_delete=models.CASCADE)
    bonus = models.CharField(max_length=1, blank=True, null=True, choices=WEAKNESS_CHOICES, default='+')
    percent = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.magic_school.name

class BlueFlagsStep(auto_prefetch.Model):
    flag = auto_prefetch.ForeignKey(BlueFlags, null=False, blank=False, on_delete=models.CASCADE)
    adventure = auto_prefetch.ForeignKey(Adventure, null=True, blank=True, on_delete=models.CASCADE)
    weapon = auto_prefetch.ForeignKey(Weapon, null=True, blank=True, on_delete=models.CASCADE, default=None)
    gathering = auto_prefetch.ForeignKey(Gathering, null=True, blank=True, on_delete=models.CASCADE, default=None)
    is_fight = models.BooleanField(blank=True, null=True, default=False)
    monster1 = auto_prefetch.ForeignKey(Monster, blank=True, null=True, on_delete=models.CASCADE, default=None, related_name="monster1")
    monster2 = auto_prefetch.ForeignKey(Monster, blank=True, null=True, on_delete=models.CASCADE, default=None, related_name="monster2")
    monster3 = auto_prefetch.ForeignKey(Monster, blank=True, null=True, on_delete=models.CASCADE, default=None, related_name="monster3")
    monster4 = auto_prefetch.ForeignKey(Monster, blank=True, null=True, on_delete=models.CASCADE, default=None, related_name="monster4")
    monster5 = auto_prefetch.ForeignKey(Monster, blank=True, null=True, on_delete=models.CASCADE, default=None, related_name="monster5")
    difficulty = models.IntegerField(null=True, blank=True)
    percent = models.IntegerField(default=0, null=False, blank=False)

class QuestItemLocations(auto_prefetch.Model):
    itemname = models.CharField(max_length=64, blank=False, null=False)
    flag = auto_prefetch.ForeignKey(BlueFlags, null=True, blank=True, on_delete=models.CASCADE)
    location = auto_prefetch.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    count = models.IntegerField(default=5, null=False, blank=False)
    geom = MultiPointField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True, related_name="quest_icon", on_delete=models.CASCADE)

    def __str__(self):
        if self.flag:
            return self.flag.name
        elif self.location:
            return self.location.name
        else:
            return _('-- no translation yet --')

    class Meta:
        ordering = ["flag"]

    @property
    def map_poi(self):
        if self.flag:
            tooltip = "{}<br>{} Total: {}".format(self.itemname, self.flag, self.count)
        else:
            tooltip = "{}<br>{} Total: {}".format(self.itemname, self.location, self.count)
        return tooltip

    @property
    def coordinates(self):
        if self.geom:
            return str(self.geom['coordinates']).replace('[', '').replace(']', '').replace(' ', '')
        else:
            return None

    @property
    def icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return None


class Cosmetics(auto_prefetch.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    value = models.IntegerField(default=1)
    price = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    location = auto_prefetch.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    npc = auto_prefetch.ForeignKey(NPC, on_delete=models.CASCADE, blank=True, null=True)
    blueflag = auto_prefetch.ForeignKey('BlueFlags', on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = FilerImageField(blank=True, null=True, related_name="cosmetic_image", on_delete=models.CASCADE)


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cosmetics_card', args=[str(self.id)])

    def get_location(self):
        if self.location:
            return self.location
        elif self.blueflag:
            return self.blueflag
        else:
            return None


class Book(auto_prefetch.Model):
    value = models.IntegerField(default=1)
    price = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    gathering = auto_prefetch.ForeignKey(Gathering, on_delete=models.CASCADE, blank=True, null=True)
    adventure = auto_prefetch.ForeignKey(Adventure, on_delete=models.CASCADE, blank=True, null=True)
    crafting = auto_prefetch.ForeignKey(Crafting, on_delete=models.CASCADE, blank=True, null=True)
    land = auto_prefetch.ForeignKey(Land, on_delete=models.CASCADE, blank=True, null=True)
    weapon = auto_prefetch.ForeignKey(Weapon, on_delete=models.CASCADE, blank=True, null=True)
    reputation = auto_prefetch.ForeignKey(Reputation, on_delete=models.CASCADE, blank=True, null=True)
    guild = auto_prefetch.ForeignKey(Guild, on_delete=models.CASCADE, blank=True, null=True)
    reputation_guild_value = models.IntegerField(blank=True, null=True, default=0)
    location = auto_prefetch.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    npc = auto_prefetch.ForeignKey(NPC, on_delete=models.CASCADE, blank=True, null=True)
    blueflag = auto_prefetch.ForeignKey(BlueFlags, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        ordering = ["gathering", "adventure", "crafting", "land", "weapon"]

    def __str__(self):
        if self.gathering:
            return '{} +{}'.format(self.gathering, self.value)
        elif self.adventure:
            return '{} +{}'.format(self.adventure, self.value)
        elif self.crafting:
            return '{} +{}'.format(self.crafting, self.value)
        elif self.land:
            return '{} +{}'.format(self.land, self.value)
        elif self.weapon:
            return '{} +{}'.format(self.weapon, self.value)

    def get_absolute_url(self):
        return reverse('book_card', args=[str(self.id)])

    def get_reputation(self):
        if self.reputation:
            return '{} {}'.format(self.reputation, self.reputation_guild_value)
        elif self.guild:
            return '{} {}'.format(self.guild, self.reputation_guild_value)

    def get_location(self):
        if self.location:
            return self.location
        elif self.blueflag:
            return self.blueflag
        else:
            return None
