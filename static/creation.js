var baseURL = 'https://www.dnd5eapi.co/api/';

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

/*
    var character = {
        "name":characterName,
        "race":race,
        "class":characterClass,
        "intelligence":intelligence,
        "dexterity":dexterity,
        "charisma":charisma,
        "strength":strength,
        "wisdom":wisdom,
        "constitution":constitution,
        //"proficiencies":proficiencies,
        "healthPoints":hp,
        "armorClass":ac,
        "speed":speed,
        "proficiencyBonus":proficiencyBonus,
        "attackBonus":attackBonus,
        "equipment":equipment,
        "spellSaveDC":spellSave
    }

    var characterAsJSON = JSON.stringify(character);

    $ajax({
        type: "POST",
        url: '{{ 'my-ajax-test/' }}',
        data: { scrfmiddlwaretoken: '{{ csrf_token }}', text: characterAsJSON },
        success: function callback(response) {
            console.log(response);
        }
    });

    console.log(characterAsJSON);
*/
    var jsonPayload = '{"characterName: "' + characterName + '", race: "' + race + '", characterClass: "' + characterClass + '", intelligence: "' + intelligence + '", dexterity: "' + dexterity + '", charisma: "' + charisma + '", strength: "' + strength + '", wisdom: "' + wisdom + '", constitution: "' + constitution + '", proficiencies: "' + proficiencies + '", healthPoints: "' + hp + '", armorClass: "' + ac + '", speed: "' + speed + '", spellSaveDC: "' + spellSave + '", attackBonus: "' + attackBonus + '", equipment: "' + equipment + '"}"';
    var url = './insertDB.py';
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
    
    var xhr = new XMLHttpRequest();
    xhr.open("GET", completeURL, false)
    xhr.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    */
}