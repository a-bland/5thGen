from django.test import TestCase
from CharacterCreator.models import Character

# Create your tests here.
class CharacterTestcase(TestCase):
    def setUp(self):
        Character.objects.create(
            name="Fredious", 
            race="Dwarf", 
            characterClass="Barbarian", 
            intelligence=16, 
            wisdom=12, 
            charisma=10, 
            strength=16, 
            dexterity=8, 
            constitution=12, 
            athletics = True,
            acrobatics = True,
            sleightOfHand = False,
            stealth = False,
            arcana = False,
            history = False,
            investigation = False,
            nature = False,
            religion = False,
            animalHandling = False,
            insight = False,
            medicine = False,
            perception = False,
            survival = False,
            deception = False,
            intimidation = False,
            performance = False,
            persuasion = False,
            hp=12, 
            ac=16, 
            speed=30,
            spellSaveDC=10, 
            attackBonus=3,
            equipment="Armor and some stuff",
            )

        Character.objects.create(
            name="Arjun", 
            race="Elf", 
            characterClass="Wizard", 
            intelligence=16, 
            wisdom=12, 
            charisma=10, 
            strength=6, 
            dexterity=8, 
            constitution=10, 
            athletics = False,
            acrobatics = False,
            sleightOfHand = False,
            stealth = False,
            arcana = True,
            history = False,
            investigation = False,
            nature = False,
            religion = False,
            animalHandling = False,
            insight = False,
            medicine = False,
            perception = True,
            survival = False,
            deception = False,
            intimidation = False,
            performance = False,
            persuasion = False,
            hp=12, 
            ac=10, 
            speed=30,
            spellSaveDC=13, 
            attackBonus=3,
            equipment="Some wizard shit",
            )
    
    def test_get_name(self):
        fredious = Character.objects.get(name="Fredious")
        arjun = Character.objects.get(name="Arjun")
        self.assertEqual(fredious.get_name(), "Fredious")
        self.assertEqual(arjun.get_name(), "Arjun")
    
    def test_get_race(self):
        fredious = Character.objects.get(name="Fredious")
        arjun = Character.objects.get(name="Arjun")
        self.assertEqual(fredious.get_race(), "Dwarf")
        self.assertEqual(arjun.get_race(), "Elf")

    def test_get_characterClass(self):
        fredious = Character.objects.get(name="Fredious")
        arjun = Character.objects.get(name="Arjun")
        self.assertEqual(fredious.get_characterClass(), "Barbarian")
        self.assertEqual(arjun.get_characterClass(), "Wizard")

