"""Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en 
el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no."""

import math

class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class circulo:
    def __init__(self, centro, r):
        self.centro = centro
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimetro(self):
        return 2 * math.pi * self.r

    def punto_(self, punto):
        distancia_ = math.sqrt((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2)
        return distancia_ <= self.r

if __name__ == "__main__":
    centro_ = punto(7, 9)
    circulo_ = circulo(centro_, 5)
    area = circulo_.area()
    perimetro = circulo_.perimetro()
    p_ext = punto(9, 13)
    pertenece = circulo_.punto_(p_ext)
    print(f"Área del círculo: {area}")
    print(f"Perímetro del círculo: {perimetro}")
    print(f"¿El punto pertenece al círculo?: {pertenece}")