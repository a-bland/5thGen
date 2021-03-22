from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    player = models.CharField(max_length=100)
    race = models.CharField(max_length=25)
    characterClass = models.CharField(max_length=25)
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    proficiencies = models.CharField(max_length=200)
    hp = models.IntegerField()
    ac = models.IntegerField()
    speed = models.IntegerField()
    spellSaveDC = models.IntegerField()
    attackBonus = models.IntegerField()
    equipment = models.CharField(max_length=1000)


class User(models.Model):
    username = models.CharField(max_length=100)
