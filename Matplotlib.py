import numpy as np
import matplotlib.pyplot as plt

class LinealSystem:
    def __init__(self, archivo):
        self.systems = self.read_txt(archivo)

    def read_txt(self, archivo):
        systems = []
        with open(archivo, 'r') as archivo:
            A = None
            b = None
            is_A = True
            for linea in archivo:
                datos = linea.strip().split(',')
                if datos[0] == 'A':
                    A = [int(x) for x in datos[1:]]
                elif datos[0] == 'B':
                    b = [int(x) for x in datos[1:]]
                    if A is not None and b is not None:
                        systems.append((A, b))
        return systems

    def solve_system(self, opcion):
        if 1 <= opcion <= len(self.systems):
            A, b = self.systems[opcion - 1]
            n = len(b)
            m = len(A)
            degree = m // n
            A = np.array(A).reshape(n, degree)
            determinante = np.linalg.det(A)
            if determinante == 0:
                print("El sistema no tiene solución única porque la matriz A es singular.")
                return None
            x = np.linalg.solve(A, b)
            return x

    def graficar_sistema_2d(self, opcion):
        if 1 <= opcion <= len(self.systems):
            A, b = self.systems[opcion - 1]
            n = len(b)
            if n != 2:
                print("Este método solo es aplicable a sistemas de 2 incógnitas.")
                return

            x = np.linspace(-10, 10, 400)  # Valores de x para la gráfica
            y1 = (-A[0] * x + b[0]) / A[1]  # Ecuación 1
            y2 = (-A[2] * x + b[1]) / A[3]  # Ecuación 2

            plt.plot(x, y1, label="Ecuación 1", color="pink")
            plt.plot(x, y2, label="Ecuación 2", color="blue")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend()
            plt.grid()
            plt.title('Gráfica del Sistema de Ecuaciones')
            plt.show()


    def run_solver(self):
        while True:
            print("Seleccione una opción:")
            print("1. Resolver sistema de ecuaciones")
            print("2. Graficar sistema 2D")
            print("3. Salir")
            opcion = input("Ingrese el número de la opción: ")

            if opcion == '3':
                print("Ha salido del programa.")
                break

            try:
                opcion = int(opcion)
            except ValueError:
                print("Opción no válida. Debe ingresar 1, 2 o 3.")
                continue

            if opcion == 1:
                print("Seleccione un sistema para resolver:")
                for i, (A, b) in enumerate(self.systems):
                    A_str = ' '.join(map(str, A))
                    b_str = ' '.join(map(str, b))
                    print(f"{i + 1}. A= [ {A_str} ] b= [ {b_str} ]")
                print(f"{len(self.systems) + 1}. Volver al menú principal")
                opcion = input("Ingrese el número del sistema que desea resolver: ")
                try:
                    opcion = int(opcion)
                except ValueError:
                    print("Opción no válida. Debe ingresar un número entre 1 y {} o {} para volver al menú principal.".format(len(self.systems), len(self.systems) + 1))
                    continue
                if 1 <= opcion <= len(self.systems):
                    x = self.solve_system(opcion)
                    if x is not None:
                        print(f"Solución del sistema de ecuaciones {opcion}:")
                        print(x.reshape(-1, 1))
                    else:
                        print(f"El sistema no tiene solución única.")
                else:
                    print("Opción no válida. Debe ingresar un número entre 1 y {} o {} para volver al menú principal.".format(len(self.systems), len(self.systems) + 1))
            elif opcion == 2:
                print("Seleccione un sistema para graficar:")
                for i, (A, b) in enumerate(self.systems):
                    A_str = ' '.join(map(str, A))
                    b_str = ' '.join(map(str, b))
                    print(f"{i + 1}. A= [ {A_str} ] b= [ {b_str} ]")
                print(f"{len(self.systems) + 1}. Volver al menú principal")
                opcion = input("Ingrese el número del sistema que desea graficar: ")
                try:
                    opcion = int(opcion)
                except ValueError:
                    print("Opción no válida. Debe ingresar un número entre 1 and {} o {} para volver al menú principal.".format(len(self.systems), len(self.systems) + 1))
                    continue
                if 1 <= opcion <= len(self.systems):
                    self.graficar_sistema_2d(opcion)
                else:
                    print("Opción no válida. Debe ingresar un número entre 1 and {} o {} para volver al menú principal.".format(len(self.systems), len(self.systems) + 1))
            else:
                print("Opción no válida. Debe ingresar 1, 2 o 3.")

if __name__ == "__main__":
    archivo = "sistema2d.txt"
    lineal_system = LinealSystem(archivo)
    lineal_system.run_solver()
