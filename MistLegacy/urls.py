from django.contrib import admin
from django.urls import path
from front.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import include

urlpatterns = i18n_patterns(
    path('silk/', include('silk.urls', namespace='silk')),

    path('', map, name='home'),
    path('set_lang/<str:lang>', set_lang, name="set_lang"),
    path('clear_cache/', clear_cache),
    path('admin/', admin.site.urls),
    path('search', search, name='search'),
    path('map', map, name='map'),

    path('guides', guides, name='guides'),

    path('basics', basics, name='basics'),
    path('flags', flags, name='flags'),
    path('companions', companions, name='companions'),
    path('monsters', monsters, name='monsters'),
    path('boss', boss, name='boss'),
    path('regions', regions, name='regions'),
    path('locations', locations, name='locations'),
    path('books', books, name='books'),
    path('recipes', recipes, name='recipes'),
    path('talents', talents, name='talents'),
    path('cosmetics', cosmetics, name='cosmetics'),

    path('land/<int:pk>', land, name='land'),
    path('adventure/<int:pk>', adventure, name='adventure'),
    path('crafting/<int:pk>', crafting, name='crafting'),
    path('gathering/<int:pk>', gathering, name='gathering'),
    path('weapon/<int:pk>', weapon, name='weapon'),
    path('reputation/<int:pk>', reputation, name='reputation'),
    path('guild/<int:pk>', guild, name='guild'),

    path('materials/<str:material_type>', materials, name='materials'),
    path('components/<str:component_type>', components, name='components'),
    path('plants', plants, name='plants'),

    path('craft', craft, name='craft'),
    path('craft/<str:craft>', craft, name='craft'),

    #path('companion_card/<int:pk>', companion_card, name='companion_card'),
    #path('book_card/<int:pk>', book_card, name='book_card'),
    #path('talent_card/<int:pk>', talent_card, name='talent_card'),
    #path('recipe_card/<int:pk>', recipe_card, name='recipe_card'),

    path('jenniel1', jenniel1, name='jenniel1'),

    prefix_default_language=False
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
