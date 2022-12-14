from django.core.management.base import BaseCommand, CommandError
from front.models import Land, Weapon, Gathering, Adventure, Crafting, Reputation, Daytime, Region, EquipmentSlot


class Command(BaseCommand):
    help = 'Initialize data'

    def handle(self, *args, **options):
        #Land(name_en="Forest", name_fr="Forêt").save()
        #Land(name_en="Mists", name_fr="Brumes").save()
        #Land(name_en="Mountain", name_fr="Montagne").save()
        #Land(name_en="Swamp", name_fr="Marais").save()
        #Land(name_en="Underground", name_fr="Souterrain").save()

        #Weapon(name_en="Axe", name_fr="Hache").save()
        #Weapon(name_en="Dagger", name_fr="Dague").save()
        #Weapon(name_en="Mace", name_fr="Masse").save()
        #Weapon(name_en="Spear", name_fr="Lance").save()
        #Weapon(name_en="Sword", name_fr="Epée").save()

        #Gathering(name_en="Botany", name_fr="Botanique").save()
        #Gathering(name_en="Mining", name_fr="Minage").save()
        #Gathering(name_en="Hunting", name_fr="Chasse").save()
        #Gathering(name_en="Lumberjacking", name_fr="Coupe").save()

        #Adventure(name_en="Academic", name_fr="Académie").save()
        #Adventure(name_en="Athletics", name_fr="Athlétisme").save()
        #Adventure(name_en="Exploration", name_fr="Exploration").save()
        #Adventure(name_en="Perception", name_fr="Perception").save()
        #Adventure(name_en="Persuasion", name_fr="Persuasion").save()
        #Adventure(name_en="Strategy", name_fr="Stratégie").save()
        #Adventure(name_en="Subterfuge", name_fr="Larçin").save()

        #Crafting(name_en="Forge", name_fr="Forge").save()
        #Crafting(name_en="Sewing", name_fr="Couture").save()
        #Crafting(name_en="Stoneworking", name_fr="Taille").save()
        #Crafting(name_en="Woodworking", name_fr="Ebenisterie").save()
        #Crafting(name_en="Tanning", name_fr="Tannage").save()

        #Reputation(name_en="Gantras", name_fr="Gantras").save()
        #Reputation(name_en="Goodneigbhor", name_fr="Bonvoisin").save()
        #Reputation(name_en="Kortombe", name_fr="Kortombe").save()
        #Reputation(name_en="Larcen", name_fr="Larcen").save()
        #Reputation(name_en="Thorval", name_fr="Thorval").save()

        #Daytime(name_en="Night", name_fr="Nuit").save()
        #Daytime(name_en="Day", name_fr="Jour").save()
        #Daytime(name_en="Always", name_fr="Permanent").save()

        EquipmentSlot(name_en="Hat", name_fr="Chapeau").save()
        EquipmentSlot(name_en="Torso", name_fr="Torse").save()
        EquipmentSlot(name_en="Gloves", name_fr="Gants").save()
        EquipmentSlot(name_en="Legs", name_fr="Jambes").save()
        EquipmentSlot(name_en="Boots", name_fr="Bottes").save()
        EquipmentSlot(name_en="Weapon", name_fr="Arme").save()
        EquipmentSlot(name_en="Lantern", name_fr="Lanterne").save()
        EquipmentSlot(name_en="Cape", name_fr="Cape").save()
        EquipmentSlot(name_en="Coat", name_fr="Surcot").save()
        EquipmentSlot(name_en="Shirt", name_fr="Chemise").save()
        EquipmentSlot(name_en="Pants", name_fr="Pantalon").save()
        EquipmentSlot(name_en="Shield", name_fr="Bouclier").save()
        EquipmentSlot(name_en="Ring", name_fr="Anneau").save()
        EquipmentSlot(name_en="Pendant", name_fr="Pendentif").save()
        EquipmentSlot(name_en="Bracelet", name_fr="Bracelet").save()
        EquipmentSlot(name_en="Serum", name_fr="Sérum").save()

        #Region(name_fr="Boisé d'Enorwen", name_en="Enorwen woodland").save()
        #Region(name_fr="Boisé de la couronne", name_en="Crown woodland").save()
        #Region(name_fr="Boisé des Fables", name_en="Woody Fables").save()
        #Region(name_fr="Boisé des Oubliés", name_en="Forest of the Forgotten").save()
        #Region(name_fr="Boisé des Tournis", name_en="Wooded Tournis").save()
        #Region(name_fr="Boisé du Marteau", name_en="Wooded area of ​​Marteau").save()
        #Region(name_fr="Boisé Duverger", name_en="Wooded Duverger").save()
        #Region(name_fr="Boisé Finorgan", name_en="Woody Finorgan").save()
        #Region(name_fr="Boisés Astridielle", name_en="Woody Astridielle").save()
        #Region(name_fr="Boisés de Dantrin", name_en="Wooded areas of Dantrin").save()
        #Region(name_fr="Boisés Des Dryades", name_en="Woodlands Des Dryades").save()
        #Region(name_fr="Boisés des Ecorché", name_en="Woodlands of Ecorché").save()
        #Region(name_fr="Boisés des Larçons", name_en="Larçons woodlands").save()
        #Region(name_fr="Boisés Donpa", name_en="Wooded Donpa").save()
        #Region(name_fr="Bouclier d'Astrid", name_en="Shield of Astrid").save()
        #Region(name_fr="Butte de l'enclume", name_en="Anvil Butte").save()
        #Region(name_fr="Butte de la scène", name_en="Butte of the stage").save()
        #Region(name_fr="Butte du Marteau", name_en="Butte du Marteau").save()
        #Region(name_fr="Butte du Sorcier", name_en="Wizard's Mound").save()
        #Region(name_fr="Canyon d'Irlandun", name_en="Irlandun Canyon").save()
        #Region(name_fr="caverne gremanir", name_en="gremanir cave").save()
        #Region(name_fr="caverne gremanir", name_en="Kortombe Plain").save()
        #Region(name_fr="Colline d'haularken", name_en="Haularken hill").save()
        #Region(name_fr="Colline de la tete de pipe", name_en="Pipe head hill").save()
        #Region(name_fr="Colline du Leviathan", name_en="Leviathan Hill").save()
        #Region(name_fr="Colline du Mur vivant", name_en="Hill of the Living Wall").save()
        #Region(name_fr="Colline Muranios", name_en="Muranios Hill").save()
        #Region(name_fr="Collines de Kortombe", name_en="Kortombe Hills").save()
        #Region(name_fr="Collines de la couronne", name_en="Crown hills").save()
        #Region(name_fr="Collines de Ridand'hok", name_en="Ridand'hok Hills").save()
        #Region(name_fr="Collines du Chevalier", name_en="Knight's Hills").save()
        #Region(name_fr="Collines Rinodor", name_en="Rinodor Hills").save()
        #Region(name_fr="Enorwen", name_en="Enorwen").save()
        #Region(name_fr="Foret d'Haularken", name_en="Haularken Forest").save()
        #Region(name_fr="Foret de Bonarcane", name_en="Bonarcane forest").save()
        #Region(name_fr="Foret de Caledorn", name_en="Caledorn Forest").save()
        #Region(name_fr="Foret de Maladorn", name_en="Maladorn Forest").save()
        #Region(name_fr="Foret de Malarcane", name_en="Malarcane forest").save()
        #Region(name_fr="Foret de Rinosaldor", name_en="Rinosaldor forest").save()
        #Region(name_fr="Foret du mur vivant", name_en="Living Wall Drill").save()
        #Region(name_fr="Foret du petit Supon", name_en="Little Supon forest").save()
        #Region(name_fr="Marais des Salamandres", name_en="Salamander Marshes").save()
        #Region(name_fr="Marecage de Quarazza", name_en="Quarazza swamp").save()
        #Region(name_fr="Mareécage de Tarinna", name_en="Tarinna Pond").save()
        #Region(name_fr="Montagne Arwell", name_en="Arwell Mountain").save()
        #Region(name_fr="Monticules des pages", name_en="Mounds of Pages").save()
        #Region(name_fr="Monts ridicule", name_en="Ridiculous mountains").save()
        #Region(name_fr="Paline de Larçons", name_en="Paline de Larçons").save()
        #Region(name_fr="Plaine de Brumedor", name_en="Plain of Brumedor").save()
        #Region(name_fr="plaine de gantras", name_en="plain of gantras").save()
        #Region(name_fr="Plaine de Jolibarde", name_en="Jolibarde plain").save()
        #Region(name_fr="Plaine de la Voleuse", name_en="Plain of the Thief").save()
        #Region(name_fr="Plaine des Adieux", name_en="Plain of Farewells").save()
        #Region(name_fr="Plaine des Amants", name_en="Plain of Lovers").save()
        #Region(name_fr="Plaine des écorchés", name_en="Plain of the Flayed").save()
        #Region(name_fr="Plaine des Millechemises", name_en="Plain of Millechemises").save()
        #Region(name_fr="Plaine du Leviathan", name_en="Leviathan Plain").save()
        #Region(name_fr="Plaine du Marteau", name_en="Hammer Plain").save()
        #Region(name_fr="Plaine du Page", name_en="Page plain").save()
        #Region(name_fr="Plaine du silence", name_en="Plain of silence").save()
        #Region(name_fr="Plaine du Troubadour", name_en="Troubadour plain").save()
        #Region(name_fr="Plateau d'Algent", name_en="Plateau d'Algent").save()
        #Region(name_fr="Plateau de Mélandrine", name_en="Melandrine tray").save()
        #Region(name_fr="Plateau Doré", name_en="Golden Tray").save()
        #Region(name_fr="Plateau du Corsan", name_en="Corsan plateau").save()
        #Region(name_fr="Raven Marsh", name_en="Raven marsh").save()
        #Region(name_fr="Ruine vivante", name_en="Living ruin").save()
        #Region(name_fr="Sommet ridicule", name_en="Ridiculous summit").save()
        #Region(name_fr="Terres du Rismouskan", name_en="Rismouskan lands").save()
        #Region(name_fr="Val Scintillant", name_en="Shimmering Valley").save()
        #Region(name_fr="Vallée Astridielle", name_en="Astridial Valley").save()
        #Region(name_fr="Vallée d'Enorwen", name_en="Enorwen Valley").save()
        #Region(name_fr="Vallée de Dalitan", name_en="Dalitan Valley").save()
        #Region(name_fr="Vallée de la Couleuvre", name_en="Valley of the Snake").save()
        #Region(name_fr="Vallée de la Rancoeur", name_en="Rancoeur Valley").save()
        #Region(name_fr="Vallée Sancharmes", name_en="Sancharmes Valley").save()

        pass