"""Ejercicio 97: Menú bancario para consultar saldo, depositar, retirar y salir;
validar fondos suficientes.
Usa: Repetir + Según (match) + Si."""


def leer_monto(mensaje):
    while True:
        try:
            monto = float(input(mensaje))
            if monto > 0:
                return monto
            print("El monto debe ser mayor que 0.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


class CuentaBancaria:
    def __init__(self, saldo_inicial=0.0):
        self.saldo = saldo_inicial

    def consultar(self):
        return self.saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            return False
        self.saldo -= monto
        return True


class Menu:
    def __init__(self):
        self.cuenta = CuentaBancaria()

    def mostrar(self):
        print("\n--- MENÚ BANCARIO ---")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")

    def ejecutar(self):
        opcion = ""
        while opcion != "4":  # Repetir
            self.mostrar()
            opcion = input("Elige una opción: ").strip()

            match opcion:  # Según
                case "1":
                    print(f"Saldo actual: {self.cuenta.consultar():.2f}")
                case "2":
                    monto = leer_monto("Monto a depositar: ")
                    self.cuenta.depositar(monto)
                    print("Depósito realizado.")
                case "3":
                    monto = leer_monto("Monto a retirar: ")
                    if self.cuenta.retirar(monto):
                        print("Retiro realizado.")
                    else:
                        print("Fondos insuficientes.")
                case "4":
                    print("¡Gracias por usar el banco!")
                case _:
                    print("Opción inválida.")


if __name__ == "__main__":
    Menu().ejecutar()
