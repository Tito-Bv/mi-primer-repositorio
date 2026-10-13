"""Ejercicio 100: Menú para factorial, tabla de multiplicar, paridad y cuadrado;
repetir hasta Salir.
Usa: Repetir + Según (match) + Si."""


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")


class Operaciones:
    @staticmethod
    def factorial(n):
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    @staticmethod
    def tabla_multiplicar(n, limite=10):
        return [f"{n} x {i} = {n * i}" for i in range(1, limite + 1)]

    @staticmethod
    def es_par(n):
        return n % 2 == 0

    @staticmethod
    def cuadrado(n):
        return n ** 2


class Menu:
    def mostrar(self):
        print("\n--- MENÚ ---")
        print("1. Factorial")
        print("2. Tabla de multiplicar")
        print("3. Paridad")
        print("4. Cuadrado")
        print("5. Salir")

    def ejecutar(self):
        opcion = ""
        while opcion != "5":  # Repetir
            self.mostrar()
            opcion = input("Elige una opción: ").strip()

            match opcion:  # Según
                case "1":
                    n = leer_entero("Número: ")
                    if n < 0:
                        print("El factorial no está definido para negativos.")
                    else:
                        print(f"{n}! = {Operaciones.factorial(n)}")
                case "2":
                    n = leer_entero("Número: ")
                    for linea in Operaciones.tabla_multiplicar(n):
                        print(linea)
                case "3":
                    n = leer_entero("Número: ")
                    if Operaciones.es_par(n):
                        print(f"{n} es par.")
                    else:
                        print(f"{n} es impar.")
                case "4":
                    n = leer_entero("Número: ")
                    print(f"{n}² = {Operaciones.cuadrado(n)}")
                case "5":
                    print("¡Hasta luego!")
                case _:
                    print("Opción inválida.")


if __name__ == "__main__":
    Menu().ejecutar()
