"""Punto 3 A la clase del punto anterior, defínale los siguientes métodos:
- Un método mostrar que imprima por consola las coordenadas del punto
- Un método mover que cambie las coordenadas del punto
- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto."""

import math

class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y



    def mostrar(self):
        print(f"eje: ({self.x}, {self.y})")



    def mover(self, px, py):
        self.x = px
        self.y = py



    def calcular(self, p_2):
        distancia = math.sqrt((self.x - p_2.x) ** 2 + (self.y - p_2.y) ** 2)
        return distancia



if __name__ == "__main__":
    p_x = punto(4, 6)
    p_x.mostrar()
    p_x.mover(8, 3)
    p_x.mostrar()
    p_y = punto(-5, 9)
    p_y.mostrar()
    distancia = p_x.calcular(p_y)
    
    
    print(f"La distancia de ejes es: {distancia}")
    