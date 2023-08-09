"""Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. 
Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado."""



class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class rectangulo:
    def __init__(self, p_1, p_2):
        self.extremo_1 = p_1
        self.extremo_2 = p_2

    def lado(self):
        return abs(self.extremo_2.x - self.extremo_1.x)

    def altura(self):
        return abs(self.extremo_2.y - self.extremo_1.y)


    def area(self):
        lado = self.lado()
        altura = self.altura()
        return lado * altura
    

    def perimetro(self):
        lado = self.lado()
        altura = self.altura()
        return 2 * (lado + altura)


    def cuadrado(self):
        lado = self.lado()
        altura = self.altura()
        return lado == altura
    
if __name__ == "__main__":
    esquina1 = punto(6, 11)
    esquina2 = punto(7, 13)
    rectangulo_ = rectangulo(esquina1, esquina2)
    area = rectangulo_.area()
    perimetro = rectangulo_.perimetro()
    cuadrado_ = rectangulo_.cuadrado()
    print(f"Perímetro del rectángulo: {perimetro}")
    print(f"Área del rectángulo: {area}")
    print(f"¿El rectángulo es un cuadrado?: {cuadrado_}")