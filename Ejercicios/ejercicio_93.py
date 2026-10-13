"""Ejercicio 93: Solicitar notas de estudiantes hasta finalizar y calcular
promedio, mayor y menor.
Usa: Mientras + Si.
Para finalizar, ingresa -1."""


def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


class RegistroNotas:
    CENTINELA = -1

    def __init__(self):
        self.suma = 0.0
        self.cantidad = 0
        self.mayor = None
        self.menor = None

    def agregar(self, nota):
        self.suma += nota
        self.cantidad += 1
        if self.mayor is None or nota > self.mayor:
            self.mayor = nota
        if self.menor is None or nota < self.menor:
            self.menor = nota

    def leer_notas(self):
        nota = leer_numero("Nota (0-100, -1 para finalizar): ")
        while nota != self.CENTINELA:
            if 0 <= nota <= 100:
                self.agregar(nota)
            else:
                print("La nota debe estar entre 0 y 100.")
            nota = leer_numero("Nota (0-100, -1 para finalizar): ")

    def mostrar_resultado(self):
        if self.cantidad == 0:
            print("\nNo se ingresaron notas.")
            return
        print(f"\nCantidad de notas: {self.cantidad}")
        print(f"Promedio: {self.suma / self.cantidad:.2f}")
        print(f"Nota mayor: {self.mayor}")
        print(f"Nota menor: {self.menor}")


if __name__ == "__main__":
    registro = RegistroNotas()
    registro.leer_notas()
    registro.mostrar_resultado()
