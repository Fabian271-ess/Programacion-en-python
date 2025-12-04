from modelo_animal import animal
from modelo_animal_terrestre import animal_terrestre
from modelo_animal_aereo import animal_aereo
from modelo_animal_acuatico import animal_acuatico
from modelo_animal_anfibio import animal_anfibio

objanimal = animal("Leon","Mediano", "8 años" , "Amarillo")
objanimal.info()
print("-------------------")

objanimalterrestre = animal_terrestre("Elefante", "Grande", "10 años", "Gris", "Sabana")
objanimalterrestre.info()
print("-------------------")

objanimalaereo = animal_aereo("Aguila","Mediano", "6 años" ,"Marron", 200)
objanimalaereo.info()
print("-------------------")

objanimalacuatico = animal_acuatico("Delfin","Grande", "5 años","Gris", "500 metros")
objanimalacuatico.info()
print("-------------------")

objanimalanfibio = animal_anfibio("Rana","Pequeño", "3 años", "Verde", "Tierra Humeda")
objanimalanfibio.info()
