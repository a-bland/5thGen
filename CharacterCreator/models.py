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
    athletics = models.BooleanField()
    acrobatics = models.BooleanField()
    sleightOfHand = models.BooleanField()
    stealth = models.BooleanField()
    arcana = models.BooleanField()
    history = models.BooleanField()
    investigation = models.BooleanField()
    nature = models.BooleanField()
    religion = models.BooleanField()
    animalHandling = models.BooleanField()
    insight = models.BooleanField()
    medicine = models.BooleanField()
    perception = models.BooleanField()
    survival = models.BooleanField()
    deception = models.BooleanField()
    intimidation = models.BooleanField()
    performance = models.BooleanField()
    persuasion = models.BooleanField()
    hp = models.IntegerField()
    ac = models.IntegerField()
    speed = models.IntegerField()
    spellSaveDC = models.IntegerField()
    attackBonus = models.IntegerField()
    equipment = models.CharField(max_length=1000)

    def get_name(self):
        return self.name
    
    def get_race(self):
        return self.race
    
    def get_characterClass(self):
        return self.characterClass


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Parties(models.Model):
    partyName = models.CharField(max_length=100)
    player1 = models.CharField(max_length=100)
    player2 = models.CharField(max_length=100)
    player3 = models.CharField(max_length=100)
    player4 = models.CharField(max_length=100)
