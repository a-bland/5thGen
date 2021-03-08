/* eslint-disable no-unused-vars */
import '../App.css';
import 'antd/dist/antd.css';
import { Typography } from 'antd';

import Amplify, { API, graphqlOperation } from 'aws-amplify';
import aws_exports from '../aws-exports.js';
Amplify.configure(aws_exports);

const { Title } = Typography;

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
                <br /><br />
                <div class="custom-select" id="class">
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
            </form>
            <br /><br />
            <a href="/"><button> Save Character </button></a>
        </div >

    );
}
function sendInfo() {
    var characterName = document.getElementById("Character Name").value;
    var race = document.getElementById("race").value;
    var jsonPayload = '{"characterName: "' + characterName + '", race: "' + race + '"}';
    var url = '/Create';

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, false);
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhr.send(jsonPayload);

}

export default Creation;