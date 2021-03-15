import Amplify, { API, graphqlOperation } from 'aws-amplify';
import aws_exports from '../aws-exports.js'; // specify the location of aws-exports.js file on your project
Amplify.configure(aws_exports);

function Battle() {
    return (
        <div className="Battle">
            <h1>Battle Simulator</h1>
            <p>Hello CHARACTER NAME!</p>
            <form>
                <input type="radio" id="standard" defaultChecked="true" name="rollType"></input>
                <label for="standard" > Standard </label>
                <input type="radio" id="advantage" name="rollType"></input>
                <label for="advantage"> Advantage </label>
                <input type="radio" id="disadvantage" name="rollType"></input>
                <label for="disadvantage"> Disadvantage </label>
            </form>
            <button onClick={rollDice}> Roll D20 </button>
            <br /><br />
            <a href="/">
                <button> End Battle </button>
            </a>
        </div>

    );
}
function rollDice() {
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
export default Battle;
