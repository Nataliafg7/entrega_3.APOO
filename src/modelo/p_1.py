#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class vehiculo:
    def __init__(self, velocidad_max, kilometraje):
        self.velocidad_max = velocidad_max
        self.kilometraje = kilometraje

carro_1 = vehiculo ("200km/h", "100km")
carro_2 = vehiculo ("150km/h", "0km")


print (f"la velocidad maxima del carro 1 es: {carro_1.velocidad_max} con un kilometraje de: {carro_1.kilometraje}")
print (f"la velocidad maxima del carro 2 es: {carro_2.velocidad_max} con un kilometraje de: {carro_2.kilometraje}")
