"""Punto 6 Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción 
del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta."""

class Carta:
    tipo = ("copas", "espada", "moneda","bastos")




    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta




if __name__ == "__main__":
    carta_ = Carta(7, Carta.tipo[1])
    print(f"numero de la carta: {carta_.valor}")
    print(f"tipo de la carta: {carta_.pinta}")
