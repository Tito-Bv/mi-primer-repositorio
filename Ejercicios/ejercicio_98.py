"""Ejercicio 98: Ingresar 10 notas, clasificar aprobadas/reprobadas y mostrar estadísticas.
Usa: Para + Si."""


def leer_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 100:
                return nota
            print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")


class AnalisisNotas:
    NOTA_APROBACION = 51

    def __init__(self, cantidad=10):
        self.cantidad = cantidad
        self.aprobadas = 0
        self.reprobadas = 0
        self.suma = 0.0
        self.mayor = None
        self.menor = None

    def leer_notas(self):
        for i in range(1, self.cantidad + 1):
            nota = leer_nota(f"Nota {i}: ")
            self.suma += nota

            if nota >= self.NOTA_APROBACION:
                self.aprobadas += 1
            else:
                self.reprobadas += 1

            if self.mayor is None or nota > self.mayor:
                self.mayor = nota
            if self.menor is None or nota < self.menor:
                self.menor = nota

    def mostrar_estadisticas(self):
        print("\n--- ESTADÍSTICAS ---")
        print(f"Aprobadas: {self.aprobadas}")
        print(f"Reprobadas: {self.reprobadas}")
        print(f"Promedio: {self.suma / self.cantidad:.2f}")
        print(f"Nota mayor: {self.mayor}")
        print(f"Nota menor: {self.menor}")


if __name__ == "__main__":
    analisis = AnalisisNotas()
    analisis.leer_notas()
    analisis.mostrar_estadisticas()
