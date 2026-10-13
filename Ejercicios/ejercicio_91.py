"""Ejercicio 91: Calculadora que permita realizar operaciones hasta seleccionar Salir.
Usa: Repetir + Según (match)."""


def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return None
        return a / b


class Menu:
    def __init__(self):
        self.calculadora = Calculadora()

    def mostrar(self):
        print("\n--- CALCULADORA ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

    def ejecutar(self):
        opcion = ""
        while opcion != "5":  # Repetir
            self.mostrar()
            opcion = input("Elige una opción: ").strip()

            match opcion:  # Según
                case "1" | "2" | "3" | "4":
                    a = leer_numero("Primer número: ")
                    b = leer_numero("Segundo número: ")
                    match opcion:
                        case "1":
                            resultado = self.calculadora.sumar(a, b)
                        case "2":
                            resultado = self.calculadora.restar(a, b)
                        case "3":
                            resultado = self.calculadora.multiplicar(a, b)
                        case "4":
                            resultado = self.calculadora.dividir(a, b)
                    if resultado is None:
                        print("Error: no se puede dividir entre cero.")
                    else:
                        print(f"Resultado: {resultado}")
                case "5":
                    print("¡Hasta luego!")
                case _:
                    print("Opción inválida.")


if __name__ == "__main__":
    Menu().ejecutar()
