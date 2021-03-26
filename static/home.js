function showPartyForm() {
    document.getElementById("partyForm").style.display = "block";
    //document.getElementById("cancelParty").style.display = "inline";
}
function hidePartyForm() {
    window.location.href = 'http://127.0.0.1:8000/home'
    document.getElementById("partyForm").style.display = "none";
    //document.getElementById("cancelParty").style.display = "none";
}