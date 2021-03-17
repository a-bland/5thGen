/* eslint-disable no-unused-vars */
import Amplify, { API, graphqlOperation } from 'aws-amplify';
import aws_exports from '../aws-exports.js';
Amplify.configure(aws_exports);

function Battle() {
    return (
        <div className="Battle">
            <h1>Battle Simulator</h1>
            <p>CHARACTER NAME (Race Class)</p>
            <h3>HP: XX</h3>
            <h3>AC: XX</h3>
            <h3>Speed: XX</h3>
            <h4>Turn Order</h4>
            <label for="inventory">Inventory</label>
            <br />
            <input type="text" id="inventory"></input>
            <br /><br />
            <label for="spellList">Spells</label>
            <br />
            <input type="text" id="spellList"></input>
            <br /><br />
            <label for="spellSlots">Spell Slots</label>
            <br />
            <input type="text" id="spellSlots"></input>
            <br /><br />
            <label for="statusEffects">Status Effects</label>
            <br />
            <input type="text" id="statusEffects"></input>
            <form>
                <input type="radio" id="standard" defaultChecked="true" name="rollType"></input>
                <label for="standard" > Standard </label>
                <input type="radio" id="advantage" name="rollType"></input>
                <label for="advantage"> Advantage </label>
                <input type="radio" id="disadvantage" name="rollType"></input>
                <label for="disadvantage"> Disadvantage </label>
            </form>
            <button onClick={rolld20}> Roll D20 </button>
            <br /><br />
            <label for="rollNumber">Number of Dice</label>
            <input type="number" id="rollNumber" defaultValue="1" min="1"></input>
            <br />
            <label for="diceType">Type of Dice</label>
            <input type="number" id="diceType" defaultValue="6" min="2" step="2" max="100"></input>
            <br />
            <button onClick={roll}>Roll</button>
            <br /><br />
            <br /><br />
            <a href="/">
                <button> End Battle </button>
            </a>
        </div>

    );
}
function rolld20() {
    var resultOne = (Math.random() * 20) + 1;
    resultOne = resultOne - (resultOne % 1);
    if (document.getElementById('standard').checked) {
        alert(resultOne)
    }
    else {
        var resultTwo = (Math.random() * 20) + 1;
        resultTwo = resultTwo - (resultTwo % 1);
        if (document.getElementById('advantage').checked) {
            if (resultOne > resultTwo) {
                alert(resultOne)
            }
            else {
                alert(resultTwo)
            }
        }
        else if (document.getElementById('disadvantage').checked) {
            if (resultOne < resultTwo) {
                alert(resultOne)
            }
            else {
                alert(resultTwo)
            }
        }
    }

}
function roll() {
    var numDice = document.getElementById("rollNumber").value;
    var diceType = document.getElementById("diceType").value;
    var sum = 0;
    for (var i = 0; i < numDice; i++) {
        var die = Math.random() * diceType + 1;
        die = die - (die % 1);
        sum += die;
    }
    alert(sum);
}
export default Battle;
