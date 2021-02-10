from modeltranslation.translator import register, TranslationOptions
from .models import Region, Reputation, Location, Recipe, Book, Training, Weapon, Land, Gathering, Adventure, Crafting, RecipeType


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


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Reputation)
class ReputationTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(RecipeType)
class RecipeTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Location)
class LocationTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Recipe)
class RecipeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Training)
class TrainingTranslationOptions(TranslationOptions):
    fields = ('name',)
