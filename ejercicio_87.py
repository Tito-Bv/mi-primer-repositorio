"""Ejercicio 87: Leer 10 números y determinar el mayor y el menor.
Usa: Para + Si + Asignar."""


def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


class MayorMenor:
    def __init__(self, cantidad=10):
        self.cantidad = cantidad
        self.mayor = None
        self.menor = None

    def leer_numeros(self):
        for i in range(1, self.cantidad + 1):
            numero = leer_numero(f"Número {i}: ")
            if self.mayor is None:
                self.mayor = numero
                self.menor = numero
            else:
                if numero > self.mayor:
                    self.mayor = numero
                if numero < self.menor:
                    self.menor = numero

    def mostrar_resultado(self):
        print(f"\nMayor: {self.mayor}")
        print(f"Menor: {self.menor}")


if __name__ == "__main__":
    app = MayorMenor()
    app.leer_numeros()
    app.mostrar_resultado()
