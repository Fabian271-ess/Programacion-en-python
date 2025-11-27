from modelo_vehiculoo import modelo_vehiculo
from modelo_vehiculo_personal import vehiculo_personal
from modelo_vehiculo_deportivo import vehiculo_deportivo
from modelo_vehiculo_carga import vehiculo_carga

objvehiculo = modelo_vehiculo("bosbawen", "Gris", 4, 5)
objvehiculo.info()
print("-------------------")

objvehiculopersonal = vehiculo_personal("Toyota", "Rojo", 4, 4, "V8", "Gasolina")
objvehiculopersonal.info_personal()
print("-------------------")

objvehiculodeportivo = vehiculo_deportivo("Ferrari", "Amarillo", 2, 2, 300, 500)
objvehiculodeportivo.info_deportivo()
print("-------------------")

objvehiculocarga = vehiculo_carga("bolqueta", "Blanco", 2, 3, 2000, "Contenedores")
objvehiculocarga.info_carga()
print("-------------------")