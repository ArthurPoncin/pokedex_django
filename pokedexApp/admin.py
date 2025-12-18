from django.contrib import admin
from .models import Pokemon, Type

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'pokedex_id', 'hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed')
    search_fields = ('name',)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass