from pyscript import document
import random

   
def beolvas(event):
    felhasznalo = document.querySelector("#beviteli-mezo").value
    document.querySelector("#kimenet1").innerText = felhasznalo