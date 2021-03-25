var baseURL = 'https://www.dnd5eapi.co/api/';

function submitForm() {
    document.getElementById("creationForm").submit();
    document.location.href = "http://127.0.0.1:8000/home";
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