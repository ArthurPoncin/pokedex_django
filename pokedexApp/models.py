from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Ability(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    # Infos
    pokedex_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    image_url = models.URLField()
    height = models.IntegerField(null=True)
    weight = models.FloatField(null=True)

    # Stats
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()

    types = models.ManyToManyField(Type)
    abilities = models.ManyToManyField(Ability)

    def __str__(self):
        return self.name
    
    # Liste des stats pour l'affichage
    @property
    def stats_as_list(self):
        MAX_STAT = 170
        
        def get_percent(val):
            return (val / MAX_STAT) * 100

        return [
            {'name': 'HP', 'value': self.hp, 'percent': get_percent(self.hp)},
            {'name': 'Attack', 'value': self.attack, 'percent': get_percent(self.attack)},
            {'name': 'Defense', 'value': self.defense, 'percent': get_percent(self.defense)},
            {'name': 'Sp. Atk', 'value': self.special_attack, 'percent': get_percent(self.special_attack)},
            {'name': 'Sp. Def', 'value': self.special_defense, 'percent': get_percent(self.special_defense)},
            {'name': 'Speed', 'value': self.speed, 'percent': get_percent(self.speed)},
        ]