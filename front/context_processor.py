from .models import Location, Region, BlueFlags, Elixir, GatheringPoint, Somberseason, Boss, QuestItemLocations
from django.db.models import Prefetch

def geojson_locations(request):
    return {'geojson_locations': Location.objects.prefetch_related('icon', 'region', 'companion_set', 'training_set', 'book_set', 'recipe_set', 'talent_set', 'boss_set').all().filter(boss__isnull=True).distinct()}


def geojson_regions(request):
    return {'geojson_regions': Region.objects.prefetch_related('land', 'monster_set').all()}


def geojson_blueflags(request):
    return {'geojson_blueflags': BlueFlags.objects.prefetch_related('icon', 'blueflagsreward_set', 'blueflagsstep_set', 'book_set', 'recipe_set').all()}


def geojson_elixirs(request):
    return {'geojson_elixirs': Elixir.objects.all()}


def geojson_gatheringpoints(request):
    return {'geojson_gatheringpoints': GatheringPoint.objects.select_related('material__icon','plant__icon', 'plant', 'material', 'material__material_type', 'material__material_type__gathering').all()}


def geojson_somberseason(request):
    return {'geojson_somberseason': Somberseason.objects.all()}


def geojson_boss(request):
    return {'geojson_boss': Location.objects.prefetch_related('icon', 'region', 'companion_set', 'training_set', 'book_set', 'recipe_set', 'talent_set', 'boss_set').all().filter(boss__isnull=False).distinct()}


def geojson_questitemlocations(request):
    return {'geojson_questitemlocations': QuestItemLocations.objects.select_related('icon').all()}
