class Being:
    def __init__(self, category, name, stats, features, speed, attacks, armorClass, health, inventory, skills):
        self.category = category
        self.name = name 
        self.stats = stats 
        self.features = features 
        self.speed = speed 
        self.attacks = attacks 
        self.armorClass = armorClass
        self.health = health
        self.inventory = inventory
        self.skills = skills

    def heal(amount):
        self.health += amount

    def damage(amount):

    def addItem(it):
        

    def removeItem(it):


class Monster:
    def __init__(self, category, species, challengeRating):
        self.category = category
        self.species = species
        self.challengeRating = challengeRating

class Character:
    def __init__(self, category, race, characterClass, spellSlots, spells, proficiencies):
        self.category = category
        self.race = race
        self.characterClass = characterClass
        self.spellSlots = spellSlots
        self.spells = spells 



class User:
    def __init__(self, category, email, username, pwHash, characters):
        self.category = category
        self.email = email 
        self.username = username
        self.pwHash = pwHash
        self.characters = characters

    def joinParty():

    def changePassword():

    def deleteAccount():

    def changeEmail():

    def makeCharacter():

    def deleteCharacter():
    

class Party:
    def __init__(self, category, players, dungeonMaster):
        self.category = category 
        self.players = players 
        self.dungeonMaster = dungeonMaster

    def removePlayer():

    def addPlayer():


class Effect:
    def __init__(self, category, name, description):
        self.category = category
        self.name = name 
        self.description = description


class Skill:
    def __init__(self, category, ability, skillModifier, isProficient):
        self.category = category
        self. ability = ability
        self. skillModifier = skillModifier
        self.isProficient = isProficient


class Spell:
    def __init__(self, category, name, level, description):
        self.category = category
        self.name = name 
        self.level = level
        self.description = description

    def cast():


class Feature:
    def __init__(self, category, name, description):
        self.category = category
        self.name = name 
        self.description = description


class Attack:
    def __init__(self, attackType, damageType, diceNum, diceType, damageMod):
        self.attackType = attackType
        self.damageType = damageType
        self.diceNum = diceNum
        self.diceType = diceType
        self.damageMod = damageMod


class Item:
    def __init__(self, category, quantity, name, value, description):
        self.category = category
        self.quantity = quantity
        self.name = name 
        self.value = value 
        self.description = description


class Weapon:
    def __init__(self, category, attacks);
        self.category = category
        self.attacks = attacks


class Armor:
    def __init__(self, category, armorClassBonus):
        self.category = category
        self.armorClassBonus = armorClassBonus


