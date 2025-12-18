from django.shortcuts import render
from django.http import HttpResponse

import requests


# Create your views here.
def hello(request):
    text = "<h1> Hello world ! </h1>"
    return HttpResponse(text)

def index(request):
    url = 'https://pokeapi.co/api/v2/pokemon?limit=151'
    response = requests.get(url)
    data = response.json()    
    pokemons = data['results']

    for pokemon in pokemons:
        pokemon_id = pokemon['url'].split('/')[-2]

        pokemon['id'] = pokemon_id
        pokemon['image'] = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png"
    
    context = {
        'pokemon_list': pokemons,
    }
    
    return render(request, 'pokedexApp/index.html', context)

def details(request, name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)
    data = response.json()
    
    data['image'] = data['sprites']['other']['official-artwork']['front_default']
    
    data['type_names'] = [t['type']['name'] for t in data['types']]

    context = {
        'pokemon': data,
    }
    
    return render(request, 'pokedexApp/details.html', context)