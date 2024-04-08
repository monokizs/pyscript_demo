from pyscript import document

document.getElementById("kimenet").innerText="Sanyi"

def beolvas(event):
    felhasznalo = document.querySelector("#beviteli-mezo").value
    document.querySelector("#kimenet1").innerText = felhasznalo