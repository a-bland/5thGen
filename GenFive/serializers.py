from django.contrib.auth.models import User, Group
from rest_framework import serializers
from CharacterCreator.models import Character


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'race', 'characterClass', 'wisdom', 'charisma', 'strength', 'dexterity', 'constitution',
                  'intelligence', 'hp', 'ac', 'attackBonus', 'speed', 'spellSaveDC', 'equipment', 'athletics', 'arcana', 'investigation', 'nature', 'religion', 'history', 'stealth', 'sleightOfHand', 'acrobatics', 'performance', 'deception', 'intimidation', 'persuasion', 'insight', 'animalHandling', 'medicine', 'survival', 'perception', 'attackBonus']
