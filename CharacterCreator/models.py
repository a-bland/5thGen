from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    player = models.CharField(max_length=100)
    race = models.CharField(max_length=25)
    characterClass = models.CharField(max_length=25)
    level = models.IntegerField()
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


class Spells(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    higher_level = models.CharField(max_length=100)
    spellRange = models.CharField(max_length=100)
    components = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    ritual = models.BooleanField()
    duration = models.CharField(max_length=100)
    concentration = models.BooleanField()
    castingTime = models.CharField(max_length=100)
    level = models.IntegerField()
    attack_type = models.CharField(max_length=20)
    damageType = models.CharField(max_length=100)
    savingThrow = models.CharField(max_length=25)

    bard = models.BooleanField()
    cleric = models.BooleanField()
    druid = models.BooleanField()
    paladin = models.BooleanField()
    ranger = models.BooleanField()
    sorcerer = models.BooleanField()
    warlock = models.BooleanField()
    wizard = models.BooleanField()
