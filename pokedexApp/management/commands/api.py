from django.core.management.base import BaseCommand
from pokedexApp.models import Pokemon, Type, Ability
import requests

class Command(BaseCommand):
    help = 'Importe les données de l''API PokeAPI vers la base de données locale'

    def handle(self, *args, **kwargs):

        # Reset la BDD
        self.stdout.write('Nettoyage de la base...')
        Pokemon.objects.all().delete()
        Type.objects.all().delete()

        # Récupération des données
        self.stdout.write(self.style.WARNING('Importation des données...'))
        url = 'https://pokeapi.co/api/v2/pokemon?limit=251'
        res = requests.get(url)
        pokemons = res.json()['results']

        # Création des pokémons
        self.stdout.write(self.style.WARNING('Création des pokémons...'))

        for pokemon in pokemons:
            url_pokemon = pokemon['url']
            data = requests.get(url_pokemon).json()

            id = data['id']
            name = data['name']
            image_url = data['sprites']['other']['official-artwork']['front_default']

            # Création de dict pour les stats
            stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}

            # Création de l'objet
            item = Pokemon.objects.create(
                pokedex_id = id,
                name = name,
                image_url = image_url,
                height = data['height'] * 10, # cm
                weight = data['weight'] / 10, # Kg
                hp = stats.get('hp', 0),
                attack = stats.get('attack', 0),
                defense = stats.get('defense', 0),
                special_attack = stats.get('special-attack', 0),
                special_defense = stats.get('special-defense', 0),
                speed = stats.get('speed', 0),
            )

            # Ajout des types
            for type in data['types']:
                type_name = type['type']['name']
                type_obj, _ = Type.objects.get_or_create(name=type_name)
                item.types.add(type_obj)

            # Ajout des compétences
            for ab_info in data['abilities']:
                ab_name = ab_info['ability']['name']
                ability_obj, _ = Ability.objects.get_or_create(name=ab_name)
                item.abilities.add(ability_obj)
            

        self.stdout.write(self.style.SUCCESS(f'Création de {len(pokemons)} pokémons Terminés !'))