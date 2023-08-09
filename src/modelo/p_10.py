"""Punto 10 Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el 
balance de la cuenta"""

class cuenta:
    def __init__(self, n_cuenta, dueño, total):
        self.n_cuenta = n_cuenta
        self.dueño = dueño
        self.total = total

    def consignar(self, cantidad):
        if cantidad > 0:
            self.total += cantidad
            print(f"Se ha consignado {cantidad} COP en la cuenta.")
        else:
            print("la cantidad de la consignación debe ser mayor a 1.000.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.total:
            self.total -= cantidad
            print(f"Se ha retirado {cantidad} de la cuenta.")
        else:
            print("la cantidad del retiro debe ser mayor a 1.000.")

    def manejo_tarj(self):
        cuota_manejo = self.total * 0.02
        self.total -= cuota_manejo
        print(f"Se ha aplicado una cuota de manejo del 2%: {cuota_manejo} COP")

if __name__ == "__main__":
    c_1 = cuenta("562845215", ["Natalia Flórez", "Benjamín Rojas"], 700.000)
    print(f"Número de cuenta: {c_1.n_cuenta}")
    print(f"dueño: {c_1.dueño}")
    print(f"total: {c_1.total} COP")
    c_1.consignar(500.000)
    print(f"total despues de la consignación: {c_1.total} COP")
    c_1.manejo_tarj()
    print(f"Balance después de la cuota de manejo: {c_1.total} COP")
    