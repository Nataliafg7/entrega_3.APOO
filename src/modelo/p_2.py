# Punto 2 Cree una clase Punto que represente un punto en el plano cartesiano.
class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje(self):
        print(f"eje: ({self.x}, {self.y})")

if __name__ == "__main__":
    p_1 = punto(10, 13)
    p_1.eje()
    p_2 = punto(-8, -9)
    p_2.eje()