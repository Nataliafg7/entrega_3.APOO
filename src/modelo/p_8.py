"""Punto 8 para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta."""
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

if __name__ == "__main__":
    c_1 = cuenta("562845215", ["Natalia Flórez", "Benjamín Rojas"], 700.000)
    print(f"Número de cuenta: {c_1.n_cuenta}")
    print(f"dueño de la cuenta: {c_1.dueño}")
    print(f"total: {c_1.total} COP")
    c_1.consignar(600.000)
    print(f"total después de la consignación: {c_1.total} COP")