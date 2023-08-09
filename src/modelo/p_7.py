"""Punto 7 Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. 
Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros."""

class cuenta:
    def __init__(self, n_cuenta, dueño, total):
        self.n_cuenta = n_cuenta
        self.dueño = dueño
        self.total = total

if __name__ == "__main__":
    c_1 = cuenta("562845215", ["Natalia Flórez", "Benjamín Rojas"], 7000.00)
    print(f"Número de cuenta: {c_1.n_cuenta}")
    print(f"Dueño de la cuenta: {c_1.dueño}")
    print(f"Total disponible: {c_1.total} COP")
