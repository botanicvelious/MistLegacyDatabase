from modeltranslation.translator import register, TranslationOptions
from .models import Region, Reputation, Location, Recipe, Book, Training, Weapon, Land, Gathering, Adventure, Crafting, Daytime, NPC, EquipmentSlot, Companion


@register(Daytime)
class DaytimeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Gathering)
class GatheringTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Adventure)
class AdventureTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Crafting)
class CraftingTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Land)
class LandTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Weapon)
class WeaponTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(EquipmentSlot)
class EquipmentSlotTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Reputation)
class ReputationTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Location)
class LocationTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Recipe)
class RecipeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Training)
class TrainingTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(NPC)
class NPCTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Companion)
class CompanionTranslationOptions(TranslationOptions):
    fields = ('name',)
