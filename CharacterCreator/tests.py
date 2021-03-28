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
            equipment="Armor and some stuff"
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
            athletics = False,      #0
            acrobatics = False,     #1
            sleightOfHand = False,  #2
            stealth = False,        #3
            arcana = True,          #4
            history = False,        #5
            investigation = False,  #6
            nature = False,         #7
            religion = False,       #8
            animalHandling = False, #9
            insight = False,        #10
            medicine = False,       #11
            perception = True,      #12
            survival = False,       #13
            deception = False,      #14
            intimidation = False,   #15
            performance = False,    #16
            persuasion = False,     #17
            hp=12, 
            ac=10, 
            speed=30,
            spellSaveDC=13, 
            attackBonus=3,
            equipment="Some wizard shit"
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

    def test_get_characterProficiencies(self):
        fredious = Character.objects.get(name='Fredious')
        arjun = Character.objects.get(name="Arjun")

        profListFred = [False for i in range(18)]
        profListFred[0] = profListFred[1] = True

        profListArj = [False for i in range(18)]
        profListArj[4] = profListArj[12] = True

        self.assertEqual(fredious.get_characterProficiences(), profListFred)
        self.assertEqual(arjun.get_characterProficiences(), profListArj)

    def test_get_character_hp(self):
        fredious = Character.objects.get(name="Fredious")
        arjun = Character.objects.get(name="Arjun")
        self.assertEqual(fredious.get_character_hp(), 12)
        self.assertEqual(arjun.get_character_hp(), 12)

    def test_get_character_ac(self):
        fredious = Character.objects.get(name="Fredious")
        arjun = Character.objects.get(name="Arjun")
        self.assertEqual(fredious.get_character_ac(), 16)
        self.assertEqual(arjun.get_character_ac(), 10)

    def test_get_character_speed(self):
        fredious = Character.objects.get(name="Fredious")
        arjun = Character.objects.get(name="Arjun")
        self.assertEqual(fredious.get_character_speed(), 30)
        self.assertEqual(arjun.get_character_speed(), 30)

    def test_get_character_spellSaveDC(self):
        fredious = Character.objects.get(name="Fredious")
        arjun = Character.objects.get(name="Arjun")
        self.assertEqual(fredious.get_character_spellSaveDC(), 10)
        self.assertEqual(arjun.get_character_spellSaveDC(), 13)

    def test_get_character_attackBonus(self):
        fredious = Character.objects.get(name="Fredious")
        arjun = Character.objects.get(name="Arjun")
        self.assertEqual(fredious.get_character_attackBonus(), 3)
        self.assertEqual(arjun.get_character_attackBonus(), 3)

    def test_get_character_equipment(self):
        fredious = Character.objects.get(name="Fredious")
        arjun = Character.objects.get(name="Arjun")
        self.assertEqual(fredious.get_character_equipment(), "Armor and some stuff")
        self.assertEqual(arjun.get_character_equipment(), "Some wizard shit")