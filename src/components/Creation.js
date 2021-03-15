/* eslint-disable no-unused-vars */
import '../App.css';

import Amplify, { API, graphqlOperation } from 'aws-amplify';
import aws_exports from '../aws-exports.js';
Amplify.configure(aws_exports);
var baseURL = 'https://www.dnd5eapi.co/api/';
function Creation() {
    return (
        <div className="Creation">
            <h1>Create Your Character</h1>
            <p>Choose wisely!</p>
            <form action="Creation" method="post" id="CharacterCreation">
                <input type="text" placeholder="Character Name" id="characterName"></input>
                <br /><br />
                <div className="custom-select" id="race">
                    <select>
                        <option value="0">Select race:</option>
                        <option value="dwarf">Dwarf</option>
                        <option value="elf">Elf</option>
                        <option value="halfling">Halfling</option>
                        <option value="human">Human</option>
                        <option value="dragonborn">Dragonborn</option>
                        <option value="gnome">Gnome</option>
                        <option value="half-elf">Half-Elf</option>
                        <option value="half-orc">Half-Orc</option>
                        <option value="tiefling">Tiefling</option>
                    </select>
                </div>
                <br />
                <div className="custom-select">
                    <select id='characterClass' onChange={displayClassInfo}>
                        <option value="0">Select class:</option>
                        <option value="barbarian" >Barbarian</option>
                        <option value="bard">Bard</option>
                        <option value="cleric">Cleric</option>
                        <option value="druid">Druid</option>
                        <option value="fighter">Fighter</option>
                        <option value="monk">Monk</option>
                        <option value="paladin">Paladin</option>
                        <option value="ranger">Ranger</option>
                        <option value="rogue">Rogue</option>
                        <option value="sorcerer">Sorcerer</option>
                        <option value="warlock">Warlock</option>
                        <option value="wizard">Wizard</option>
                    </select>
                </div>
                <br />
                <fieldset className="stats">
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
                    <input type="checkbox" id="athletics" className="proficiencies"></input>
                    <br /><br />
                    <label for="acrobatics">Acrobatics </label>
                    <input type="checkbox" id="acrobatics" className="proficiencies"></input>
                    <br /><br />
                    <label for="sleightOfHand">Sleight of Hand </label>
                    <input type="checkbox" id="sleightOfHand" className="proficiencies"></input>
                    <br /><br />
                    <label for="stealth">Stealth </label>
                    <input type="checkbox" id="stealth" className="proficiencies"></input>
                    <br /><br />
                    <label for="arcana">Arcana </label>
                    <input type="checkbox" id="arcana" className="proficiencies"></input>
                    <br /><br />
                    <label for="history">History </label>
                    <input type="checkbox" id="history" className="proficiencies"></input>
                    <br /><br />
                    <label for="investigation">Investigation </label>
                    <input type="checkbox" id="investigation" className="proficiencies"></input>
                    <br /><br />
                    <label for="nature">Nature </label>
                    <input type="checkbox" id="nature" className="proficiencies"></input>
                    <br /><br />
                    <label for="religion">Religion</label>
                    <input type="checkbox" id="religion" className="proficiencies"></input>
                    <br /><br />
                    <label for="animalHandling">Animal Handling </label>
                    <input type="checkbox" id="animalHandling" className="proficiencies"></input>
                    <br /><br />
                    <label for="insight">Insight </label>
                    <input type="checkbox" id="insight" className="proficiencies"></input>
                    <br /><br />
                    <label for="medicine">Medicine </label>
                    <input type="checkbox" id="medicine" className="proficiencies"></input>
                    <br /><br />
                    <label for="perception">Perception </label>
                    <input type="checkbox" id="perception" className="proficiencies"></input>
                    <br /><br />
                    <label for="survival">Survival </label>
                    <input type="checkbox" id="survival" className="proficiencies"></input>
                    <br /><br />
                    <label for="deception">Deception </label>
                    <input type="checkbox" id="deception" className="proficiencies"></input>
                    <br /><br />
                    <label for="intimidation">Intimidation </label>
                    <input type="checkbox" id="intimidation" className="proficiencies"></input>
                    <br /><br />
                    <label for="performance">Performance </label>
                    <input type="checkbox" id="performance" className="proficiencies"></input>
                    <br /><br />
                    <label for="persuasion">Persuasion </label>
                    <input type="checkbox" id="persuasion" className="proficiencies"></input>
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
    var characterName = document.getElementById("characterName").value;
    var race = document.getElementById("race").value;
    var characterClass = document.getElementById("characterClass").value;
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
    var spellSave = document.getElementById("spellSave").value;

    var jsonPayload = '{"characterName: "' + characterName + '", race: "' + race + '", class: "' + characterClass + '", intelligence: "' + intelligence + '", dexterity: "' + dexterity + '", charisma: "' + charisma + '", strength: "' + strength + '", wisdom: "' + wisdom + '", constitution: "' + constitution + '", proficiencies: "' + proficiencies + '", HP: "' + hp + '", AC: "' + ac + '", speed: "' + speed + '", spellSave: "' + spellSave + '", attackBonus: "' + attackBonus + '", equipment: "' + equipment + '"}"';
    var url = 'localhost:3000/Create';

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, false);
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhr.send(jsonPayload);
}

function displayClassInfo() {
    //document.getElementById('characterClass').options[0].selected = true;
    var selectedClass = document.getElementById('characterClass').value;
    var subURL = 'classes/';
    var completeURL = baseURL + subURL + selectedClass;
    fetch(completeURL)
        .then(function (response) {
            return response.json();
        })
        .then(function (myJson) {
            console.log(myJson);
        })
        .catch(function (error) {
            console.log("Error: " + error);
        });
    /*
    fetch(completeURL)
        .then(response => response.json()),
        .then(data => console.log(data);
    //alert("The class " + selectedClass + " was selected");
    /*
    var xhr = new XMLHttpRequest();
    xhr.open("GET", completeURL, false)
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    */
}
export default Creation;