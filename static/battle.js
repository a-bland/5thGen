function rolld20() {
    var resultOne = (Math.random() * 20) + 1;
    resultOne = resultOne - (resultOne % 1);
    if (document.getElementById('standard').checked) {
        alert(resultOne)
    }
    else {
        var resultTwo = (Math.random() * 20) + 1;
        resultTwo = resultTwo - (resultTwo % 1);
        if (document.getElementById('advantage').checked || document.getElementById('disadvantage').checked) {
            alert(resultOne + " and " + resultTwo)
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