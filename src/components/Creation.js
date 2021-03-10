/* eslint-disable no-unused-vars */
import '../App.css';

import Amplify, { API, graphqlOperation } from 'aws-amplify';
import aws_exports from '../aws-exports.js';
Amplify.configure(aws_exports);

function Creation() {
    return (
        <div className="Creation">
            <h1>Create Your Character</h1>
            <p>Choose wisely!</p>
            <form action="Creation" method="post" id="CharacterCreation">
                <input type="text" placeholder="Character Name"></input>
                <br /><br />
                <div class="custom-select" id="race">
                    <select>
                        <option value="0">Select race:</option>
                        <option value="1">Dwarf</option>
                        <option value="2">Elf</option>
                        <option value="3">Halfing</option>
                        <option value="4">Human</option>
                        <option value="5">Dragonborn</option>
                        <option value="6">Gnome</option>
                        <option value="7">Half-Elf</option>
                        <option value="8">Half-Orc</option>
                        <option value="9">Tiefling</option>
                    </select>
                </div>
                <br />
                <div class="custom-select" id="characterClass">
                    <select>
                        <option value="0">Select class:</option>
                        <option value="1">Barbarian</option>
                        <option value="2">Bard</option>
                        <option value="3">Cleric</option>
                        <option value="4">Druid</option>
                        <option value="5">Fighter</option>
                        <option value="6">Monk</option>
                        <option value="7">Paladin</option>
                        <option value="8">Ranger</option>
                        <option value="9">Rogue</option>
                        <option value="10">Sorcerer</option>
                        <option value="11">Warlock</option>
                        <option value="12">Wizard</option>
                    </select>
                </div>
                <br />
                <fieldset class="stats">
                    <label for="intelligence">Intelligence </label>
                    <input type="number" min="0" max="20" id="intelligence" defaultValue="10"></input>
                    <br /><br />
                    <label for="dexterity">Dexterity </label>
                    <input type="number" min="0" max="20" id="dexterity" defaultValue="10"></input>
                    <br /><br />
                    <label for="charisma">Charisma </label>
                    <input type="number" min="0" max="20" id="charisma" defaultValue="10"></input>
                    <br /><br />
                    <label for="strength">Strength </label>
                    <input type="number" min="0" max="20" id="strength" defaultValue="10"></input>
                    <br /><br />
                    <label for="constitution">Constitution </label>
                    <input type="number" min="0" max="20" id="constitution" defaultValue="10"></input>
                    <br /><br />
                    <label for="wisdom">Wisdom </label>
                    <input type="number" min="0" max="20" id="widsom" defaultValue="10"></input>
                </fieldset>
                <br /><br />
                <fieldset>
                    <label for="athletics">Athletics </label>
                    <input type="checkbox" id="athletics" class="proficiencies"></input>
                    <br /><br />
                    <label for="acrobatics">Acrobatics </label>
                    <input type="checkbox" id="acrobatics" class="proficiencies"></input>
                    <br /><br />
                    <label for="sleightOfHand">Sleight of Hand </label>
                    <input type="checkbox" id="sleightOfHand" class="proficiencies"></input>
                    <br /><br />
                    <label for="stealth">Stealth </label>
                    <input type="checkbox" id="stealth" class="proficiencies"></input>
                    <br /><br />
                    <label for="arcana">Arcana </label>
                    <input type="checkbox" id="arcana" class="proficiencies"></input>
                    <br /><br />
                    <label for="history">History </label>
                    <input type="checkbox" id="history" class="proficiencies"></input>
                    <br /><br />
                    <label for="investigation">Investigation </label>
                    <input type="checkbox" id="investigation" class="proficiencies"></input>
                    <br /><br />
                    <label for="nature">Nature </label>
                    <input type="checkbox" id="nature" class="proficiencies"></input>
                    <br /><br />
                    <label for="religion">Religion</label>
                    <input type="checkbox" id="religion" class="proficiencies"></input>
                    <br /><br />
                    <label for="animalHandling">Animal Handling </label>
                    <input type="checkbox" id="animalHandling" class="proficiencies"></input>
                    <br /><br />
                    <label for="insight">Insight </label>
                    <input type="checkbox" id="insight" class="proficiencies"></input>
                    <br /><br />
                    <label for="medicine">Medicine </label>
                    <input type="checkbox" id="medicine" class="proficiencies"></input>
                    <br /><br />
                    <label for="perception">Perception </label>
                    <input type="checkbox" id="perception" class="proficiencies"></input>
                    <br /><br />
                    <label for="survival">Survival </label>
                    <input type="checkbox" id="survival" class="proficiencies"></input>
                    <br /><br />
                    <label for="deception">Deception </label>
                    <input type="checkbox" id="deception" class="proficiencies"></input>
                    <br /><br />
                    <label for="intimidation">Intimidation </label>
                    <input type="checkbox" id="intimidation" class="proficiencies"></input>
                    <br /><br />
                    <label for="performance">Performance </label>
                    <input type="checkbox" id="performance" class="proficiencies"></input>
                    <br /><br />
                    <label for="persuasion">Persuasion </label>
                    <input type="checkbox" id="persuasion" class="proficiencies"></input>
                </fieldset>
                <label for="profiencyBonus">Profiency Bonus </label>
                <input type="number" id="profiencyBonus"></input>
                <br /><br />
                <label for="spellSave">Spell Save DC </label>
                <input type="number" id="spellSave"></input>
                <br /><br />
                <label for="hp">HP </label>
                <input type="number" id="hp"></input>
                <br /><br />
                <label for="ac">Armor Class </label>
                <input type="number" id="ac"></input>
                <br /><br />
                <label for="attackBonus">Attack Bonus </label>
                <input type="number" id="attackBonus"></input>
                <br /><br />
                <label for="speed">Speed </label>
                <input type="number" id="speed"></input>
                <br /><br />
                <label for="equipment">Equipment </label>
                <input type="text" id="equipment"></input>
                <br /><br />
            </form>
            <br /><br />
            <a href="/"><button onClick={sendInfo}> Save Character </button></a>
        </div >

    );
}
function sendInfo() {
    var characterName = document.getElementById("Character Name").value;
    var race = document.getElementById("race").value;
    var characterClass = document.getElementById("class").value;
    var intelligence = document.getElementById("intelligence").value;
    var dexterity = document.getElementById("dexterity").value;
    var charisma = document.getElementById("charisma").value;
    var strength = document.getElementById("strength").value;
    var wisdom = document.getElementById("wisdom").value;
    var constitution = document.getElementById("constitution").value;

    var proficiencyInputs = document.querySelectorAll('.proficiencies');
    var proficiencies = {};
    for (var i = 0; i < proficiencies.length; i++) {
        if (proficiencyInputs[i].checked === true) {
            proficiencies.push(proficiencyInputs[i]);
        }
    }

    var hp = document.getElementById("hp").value;
    var ac = document.getElementById("ac").value;
    var speed = document.getElementById("speed").value;
    var proficiencyBonus = document.getElementById("proficiencyBonus").value;
    var attackBonus = document.getElementById("attackBonus").value;
    var equipment = document.getElementById("equipment").value;
    console.log(proficiencyInputs); //idk if the above works tbh
    var jsonPayload = '{"characterName: "' + characterName + '", race: "' + race + '", class: "' + characterClass + '", intelligence: "' + intelligence + '", dexterity: "' + dexterity + '", charisma: "' + charisma + '", strength: "' + strength + '", wisdom: "' + wisdom + '", constitution: "' + constitution + '"}';
    var url = '/Create';

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, false);
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhr.send(jsonPayload);
}
export default Creation;