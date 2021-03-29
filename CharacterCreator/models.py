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

<<<<<<< HEAD
    def get_characterProficiences(self):
        profList = [False for i in range(18)]
        profList[0] = self.athletics
        profList[1] = self.acrobatics
        profList[2] = self.sleightOfHand
        profList[3] = self.stealth
        profList[4] = self.arcana
        profList[5] = self.history
        profList[6] = self.investigation
        profList[7] = self.nature
        profList[8] = self.religion
        profList[9] = self.animalHandling
        profList[10] = self.insight
        profList[11] = self.medicine
        profList[12] = self.perception
        profList[13] = self.survival
        profList[14] = self.deception
        profList[15] = self.intimidation
        profList[16] = self.performance
        profList[17] = self.persuasion
        return profList

    def get_character_hp(self):
        return self.hp        

    def get_character_ac(self):
        return self.ac

    def get_character_speed(self):
        return self.speed

    def get_character_spellSaveDC(self):
        return self.spellSaveDC

    def get_character_attackBonus(self):
        return self.attackBonus

    def get_character_equipment(self):
        return self.equipment  
=======
>>>>>>> latest

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
