# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from CharacterCreator.models import Character, User, Parties, Spells


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PartiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parties
        fields = ['partyName', 'player1', 'player2', 'player3', 'player4']


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'race', 'characterClass', 'level', 'wisdom', 'charisma', 'strength', 'dexterity', 'constitution',
                  'intelligence', 'hp', 'ac', 'attackBonus', 'speed', 'spellSaveDC', 'equipment', 'athletics', 'arcana', 'investigation', 'nature', 'religion', 'history', 'stealth', 'sleightOfHand', 'acrobatics', 'performance', 'deception', 'intimidation', 'persuasion', 'insight', 'animalHandling', 'medicine', 'survival', 'perception', 'attackBonus']


class SpellsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spells
        fields = ['name', 'desc', 'higher_level',
                  'spellRange', 'components', 'material', 'ritual', 'duration',  'concentration', 'castingTime', 'level', 'attack_type', 'damage_type', 'saving_throw', 'bard', 'cleric', 'druid', 'paladin', 'ranger', 'sorcerer', 'warlock', 'wizard']
