from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    # Infos
    pokedex_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    image_url = models.URLField()

    # Stats
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()

    types = models.ManyToManyField(Type)

    def __str__(self):
        return self.name