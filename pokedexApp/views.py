from django.shortcuts import render, get_object_or_404
from .models import Pokemon, Type


def index(request):
    pokemons = Pokemon.objects.all().order_by('pokedex_id')

    context = {
            'pokemon_list': pokemons,
        }
    
    return render(request, 'pokedexApp/index.html', context)

def details(request, name):
    pokemon = get_object_or_404(Pokemon, name=name)
    
    context = {
        'pokemon': pokemon,
    }
    
    return render(request, 'pokedexApp/details.html', context)