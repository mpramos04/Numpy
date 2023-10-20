import numpy as np

#Define una clase llamada 'LinealSystem'
class LinealSystem:
    def __init__(self, archivo):
        #Llama al método 'read_txt' para leer a A y b
        self.systems = self.read_txt(archivo)

    def read_txt(self, archivo): #Lee el sistema de ecuaciones
        systems = []
        with open(archivo, 'r') as archivo: #Abre el archivo y lo lee
            A = None
            b = None
            for linea in archivo:
                datos = linea.strip().split(',')
                if datos[0] == 'A':
                    #Si ya se ha encontrado una matriz A y un vector b previamente, los agrega a la lista de sistemas
                    if A is not None and b is not None:
                        systems.append((A, b))
                    A = [int(x) for x in datos[1:]]  # Cambio a números enteros
                elif datos[0] == 'B':
                    b = [int(x) for x in datos[1:]]  # Cambio a números enteros
            #Después de terminar de leer el archivo, si aún hay una matriz A y un vector b, los agrega a la lista de sistemas
            if A is not None and b is not None:
                systems.append((A, b))
        return systems

    def solve_system(self, opcion): #Método para resolver un sistema de ecuaciones específico
        if 1 <= opcion <= len(self.systems):
            #Obtiene la matriz A y el vector b del sistema seleccionado
            A, b = self.systems[opcion - 1]

            n = len(b)  # Longitud de b
            m = len(A)  # Longitud de A

            # Calcular el grado de las ecuaciones
            degree = m // n

            #Convierte la lista A en una matriz NumPy de dimensiones n x degree
            A = np.array(A).reshape(n, degree)  # Convertir A en una matriz bidimensional

            determinante = np.linalg.det(A)

            if determinante == 0:
                print("El sistema no tiene solución única porque la matriz A es singular.")
                return None
            # Resuelve el sistema de ecuaciones y almacena la solución en 'x'
            x = np.linalg.solve(A, b)

            return x

    def run_solver(self): #Método para ejecutar el programa principal
        while True:
            print("Seleccione un sistema para resolver:")
            #Muestra la lista de sistemas disponibles
            for i, (A, b) in enumerate(self.systems):
                A_str = ' '.join(map(str, A))
                b_str = ' '.join(map(str, b))
                print(f"{i + 1}. A= [ {A_str} ] b= [ {b_str} ]")
            print(f"{len(self.systems) + 1}. Salir")

            opcion = input("Ingrese el número del sistema que desea resolver: ")

            if opcion == str(len(self.systems) + 1):
                print("Ha salido del programa.")
                break

            try:
                opcion = int(opcion)
            except ValueError:
                print("Opción no válida. Debe ingresar un número entre 1 y {} o {} para salir.".format(len(self.systems), len(self.systems) + 1))
                continue

            if 1 <= opcion <= len(self.systems):
                x = self.solve_system(opcion)
                if x is not None:
                    print(f"Solución del sistema de ecuaciones {opcion}:")
                    print(x.reshape(-1, 1))
                else:
                    print(f"El sistema no tiene solución única.")
            else:
                print("Opción no válida. Debe ingresar un número entre 1 y {} o {} para salir.".format(len(self.systems), len(self.systems) + 1))

if __name__ == "__main__":
    archivo = "matrices.txt"
    lineal_system = LinealSystem(archivo)
    lineal_system.run_solver()
