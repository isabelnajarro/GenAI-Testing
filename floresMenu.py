from floresHerencia import Flor, Rosa, Amapola
import csv

class FlorManager:
    def __init__(self):
        self.csv_rosas = "rosas.csv"
        self.rosas = []
        self.csv_amapolas = "amapolas.csv"
        self.amapolas = []
        self.leer_info_rosas()
        self.leer_info_amapolas()

    def leer_info_rosas(self):
        try:
            with open(self.csv_rosas, 'r') as archivo_csv:
                lector_csv = csv.DictReader(archivo_csv)
                for fila in lector_csv:
                    rosa = Rosa(fila['Nombre'], fila['Tipo'], int(fila['HorasSol']), int(fila['HorasMaxSol']), fila['Color'])
                    self.rosas.append(rosa)
        except FileNotFoundError:
            print(f"El archivo '{self.csv_rosas}' no se encontró.")

    def leer_info_amapolas(self):
        try:
            with open(self.csv_amapolas, 'r') as archivo_csv:
                lector_csv = csv.DictReader(archivo_csv)
                for fila in lector_csv:
                    amapola = Amapola(fila['Nombre'], fila['Tipo'], int(fila['HorasSol']), int(fila['HorasMaxSol']), fila['Temporada'])
                    self.amapolas.append(amapola)
        except FileNotFoundError:
            print(f"El archivo '{self.csv_amapolas}' no se encontró.")
    
    def mostrar_rosas(self):
        for rosa in self.rosas:
            print(f"Nombre: {rosa.nombre}, Tipo: {rosa.tipo}, HorasSol: {rosa.horasSol}, HorasMaxSol: {rosa.horasMaxSol}, Color: {rosa.color}")
    
    def mostrar_amapolas(self):
        for amapola in self.amapolas:
            print(f"Nombre: {amapola.nombre}, Tipo: {amapola.tipo}, HorasSol: {amapola.horasSol}, HorasMaxSol: {amapola.horasMaxSol}, Temporada: {amapola.temporada}")

    def guardar_rosas(self, changes=False):
        try:
            with open(self.csv_rosas, 'w', newline='') as archivo:
                campos = ["Nombre", "Tipo", "HorasSol", "HorasMaxSol", "Color"]
                escritor_csv = csv.DictWriter(archivo, fieldnames=campos)

                escritor_csv.writeheader()
                for rosa in self.rosas:
                    escritor_csv.writerow({
                        "Nombre": rosa.nombre,
                        "Tipo": rosa.tipo,
                        "HorasSol": rosa.horasSol,
                        "HorasMaxSol": rosa.horasMaxSol,
                        "Color": rosa.color 
                    })
            print(f"Se han guardado los datos en '{self.csv_rosas}'.")
        except Exception as e:
            print(f"Error al guardar en '{self.csv_rosas}': {e}")

    def guardar_amapolas(self):
        try:
            with open(self.csv_amapolas, 'w', newline='') as archivo:
                campos = ["Nombre", "Tipo", "HorasSol", "HorasMaxSol", "Temporada"]
                escritor_csv = csv.DictWriter(archivo, fieldnames=campos)

                escritor_csv.writeheader()
                for amapola in self.amapolas:
                    escritor_csv.writerow({
                        "Nombre": amapola.nombre,
                        "Tipo": amapola.tipo,
                        "HorasSol": amapola.horasSol,
                        "HorasMaxSol": amapola.horasMaxSol,
                        "Temporada": amapola.temporada
                    })
            print(f"Se han guardado los datos en '{self.csv_amapolas}'.")
        except Exception as e:
            print(f"Error al guardar en '{self.csv_amapolas}': {e}")

    def actualizarBD(self):
        print("Se procede a actualizar la base de datos de rosas")
        self.guardar_rosas()
        print("Se procede a actualizar la base de datos de amapolas")
        self.guardar_amapolas()

    def addRosa(self, nombre, tipo, horasSol, horasMaxSol, color):
        rosa = Rosa(nombre, tipo, horasSol, horasMaxSol, color)
        self.rosas.append(rosa)
        self.guardar_rosas()

    def addAmapola(self, nombre, tipo, horasSol, horasMaxSol, temporada):
        amapola = Amapola(nombre, tipo, horasSol, horasMaxSol, temporada)
        self.amapolas.append(amapola)
        self.guardar_amapolas()
 
    def borrarRosa(self, nombre):
        for rosa in self.rosas:
            if rosa.nombre == nombre:
                self.rosas.remove(rosa)
                self.guardar_rosas()
                print(f"Se ha eliminado la rosa '{nombre}'.")
        print(f"No se encontró la rosa '{nombre}'.")

    def borrarAmapola(self, nombre):
        for amapola in self.amapolas:
            if amapola.nombre == nombre:
                self.amapolas.remove(amapola)
                self.guardar_amapolas()
                print(f"Se ha eliminado la amapola '{nombre}'.")
        print(f"No se encontró la amapola '{nombre}'.")

    def actualizarHorasSol(self, horas, tipo):
        if tipo == "1":
            for rosa in self.rosas:
                rosa.sumarHorasSol(horas)
            self.guardar_rosas()
        elif tipo == "2":
            for amapola in self.amapolas:
                amapola.sumarHorasSol(horas)
            self.guardar_amapolas()

    def mostrarFloresDisponibles(self):
        print("Flores disponibles")
        print("Rosas:")
        iter_rosas = iter(self.rosas)
        while True:
            try:
                rosa = next(iter_rosas)
                print(f"{rosa.nombre}: {'Disponible' if rosa.isAvailable(rosa.nombre) else 'No Disponible'}")
            except StopIteration:
                break

        print("\nAmapolas:")
        iter_amapolas = iter(self.amapolas)
        while True:
            try:
                amapola = next(iter_amapolas)
                print(f"{amapola.nombre}: {'Disponible' if amapola.isAvailable(amapola.nombre) else 'No Disponible'}")
            except StopIteration:
                break


    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Mostrar flores")
            print("2. Poner plantas al sol")
            print("3. Actualizar base de datos")
            print("4. Crear rosa")
            print("5. Crear amapola")
            print("6. Borrar flor")
            print("7. Flores disponibles")
            print("8. Salir")

            opcion = input("Selecciona opción: ")

            if opcion == "1":
                opcion = input("Selecciona 1. Rosas o 2. Amapolas: ")
                if opcion == "1":
                    self.mostrar_rosas()
                elif opcion == "2":
                    self.mostrar_amapolas()
            elif opcion == "2":
                opcion = input("Selecciona 1. Rosas o 2. Amapolas: ")
                horas = input("¿Cuántas horas quieres ponerlas al sol?")
                self.actualizarHorasSol(int(horas), opcion)
            elif opcion == "3":
                self.actualizarBD()
            elif opcion == "4":
                nombre = input("nombre de la rosa: ")
                tipo = input("tipo de la rosa: ")
                horasSol = int(input(" horas de sol de la rosa: "))
                horasMaxSol = int(input(" horas máximas de sol de la rosa: "))
                color = input("color de la rosa: ")
                self.addRosa(nombre, tipo, horasSol, horasMaxSol, color)
            elif opcion == "5":
                nombre = input("nombre de la amapola: ")
                tipo = input("tipo de la amapola: ")
                horasSol = int(input("horas de sol de la amapola: "))
                horasMaxSol = int(input("horas máximas de sol de la amapola: "))
                temporada = input("temporada de la amapola: ")
                self.addAmapola(nombre, tipo, horasSol, horasMaxSol, temporada)
            elif opcion == "6":
                opcion = input("Selecciona 1. Borrar rosa o 2. Borrar amapola: ")
                nombre = input("nombre de la flor a borrar: ")
                if opcion == "1":
                    self.borrarRosa(nombre)
                elif opcion == "2":
                    self.borrarAmapola(nombre)
            elif opcion == "7":
                self.mostrarFloresDisponibles()
            elif opcion == "8":
                break
            

if __name__ == "__main__":
    manager = FlorManager()
    manager.menu()
