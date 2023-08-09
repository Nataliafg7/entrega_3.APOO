"""Punto 11 Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por 
consola los detalles de la cuenta bancaria."""

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

    def movimientos(self):
        print("movimientos de la cuenta:")
        print(f"Número de cuenta: {self.n_cuenta}")
        print(f"dueño: {', '.join(self.dueño)}")
        print(f"total: {self.total} COP")

if __name__ == "__main__":
    c_1 = cuenta("562845215", ["Natalia Flórez", "Benjamín Rojas"], 700.000)
    c_1.movimientos()
    c_1.consignar(500.000)
    c_1.movimientos()
    c_1.manejo_tarj()
    c_1.movimientos()
    