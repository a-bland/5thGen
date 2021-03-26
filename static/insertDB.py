import json
from json import JSONEncoder
import sqlite3

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace


def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO Characters(name, race, characterClass, intelligence, dexterity, charisma, strength, wisdom, constitution, athletics, arcana, investigation, nature, religion, history, stealth, sleightOfHand, acrobatics, performance, deception, intimidation, persuasion, insight, animalHandling, medicine, survival, perception, healthPoints, armorClass, speed, spellSaveDC, attackBonus, equipment) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', entities)
    con.commit()


def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM Characters')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)


con = sqlite3.connect('../db.sqlite3')

with open('file.json', encoding='utf-8-sig') as json_file:
    text = json_file.read()
    json_data = json.loads(text, object_hook=lambda d: Namespace(**d))
    sql_insert(con, (json_data.id, json_data.name, json_data.race, json_data.characterClass, json_data.intelligence, json_data.dexterity, json_data.charisma, json_data.strength, json_data.wisdom,
               json_data.constitution, json_data.athletics, json_data.acrobatics, json_data.sleightOfHand, json_data.stealth, json_data.arcana, json_data.history, json_data.investigation, json_data.nature, json_data.religion, json_data.animalHandling, json_data.insight, json_data.medicine, json_data.perception, json_data.survival, json_data.deception, json_data.initimidation, json_data.performance, json_data.persuasion, json_data.healthPoints, json_data.armorClass, json_data.speed, json_data.spellSaveDC, json_data.attackBonus, json_data.equipment))
    con.close()
