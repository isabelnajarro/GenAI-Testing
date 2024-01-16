class Gestionpeliculas:
    def __init__(self):
        self.peliculas = {}

    def añadir_pelicula(self, nombre, director, año, presupuesto):
        if nombre not in self.peliculas:
            self.peliculas[nombre] = {'director': director, 'año': año, 'presupuesto': presupuesto}
            print(f'pelicula "{nombre}" añadida a la lista.')
        else:
            print(f'La pelicula "{nombre}" ya está en la lista.')

    def eliminar_pelicula(self, nombre):
        if nombre in self.peliculas:
            del self.peliculas[nombre]
            print(f'pelicula "{nombre}" eliminada de la lista.')
        else:
            print(f'La pelicula "{nombre}" no está en la lista.')

    def mostrar_lista_peliculas(self):
        if not self.peliculas:
            print('La lista de peliculas está vacía.')
        else:
            print('Lista de peliculas:')
            for nombre, metadatos in self.peliculas.items():
                print(f'Nombre: {nombre}, Director: {metadatos["director"]}, Año: {metadatos["año"]}, Presupuesto: {metadatos["presupuesto"]}')

    def buscar_pelicula(self, nombre):
        if nombre in self.peliculas:
            metadatos = self.peliculas[nombre]
            print(f'pelicula "{nombre}": Director: {metadatos["director"]}, Año: {metadatos["año"]}, Presupuesto: {metadatos["presupuesto"]}')
        else:
            print(f'La pelicula "{nombre}" no está en la lista.')
    
    def modificar_pelicula(self, nombre, director, año, presupuesto):
        if nombre in self.peliculas:
            self.peliculas[nombre] = {'director': director, 'año': año, 'presupuesto': presupuesto}
            print(f'Datos de la película "{nombre}" modificados.')
        else:
            print(f'La película "{nombre}" no está en la lista.')

    
    def modificar_presupuestos(self, porcentaje):
        for nombre, detalles in self.peliculas.items():
            nuevo_presupuesto = float(detalles["presupuesto"]) * (1 + porcentaje / 100)
            if nuevo_presupuesto > 0:
                detalles["presupuesto"] = nuevo_presupuesto


def main():
    gestor_peliculas = Gestionpeliculas()

    while True:
        print("\nMenu:")
        print("1. Añadir pelicula")
        print("2. Eliminar pelicula")
        print("3. Mostrar Lista de peliculas")
        print("4. Modificar pelicula")
        print("5. Buscar pelicula")
        print("6. Modificar Presupuestos")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_pelicula = input("Nombre de la pelicula: ")
            director_pelicula = input("Nombre del director: ")
            año_pelicula = input("Año de la pelicula: ")
            presupuesto_pelicula = input("Presupuesto de la pelicula: ")
            gestor_peliculas.añadir_pelicula(nombre_pelicula, director_pelicula, año_pelicula, presupuesto_pelicula)
        elif opcion == "2":
            nombre_pelicula = input("Nombre de la pelicula que deseas eliminar: ")
            gestor_peliculas.eliminar_pelicula(nombre_pelicula)
        elif opcion == "3":
            gestor_peliculas.mostrar_lista_peliculas()
        elif opcion == "4":
            nombre_pelicula = input("Nombre de la pelicula que deseas modificar: ")
            director_pelicula = input("Nuevo nombre del director: ")
            año_pelicula = input("Nuevo año de la pelicula: ")
            presupuesto_pelicula = input("Nuevo presupuesto de la pelicula: ")
            gestor_peliculas.modificar_pelicula(nombre_pelicula, director_pelicula, año_pelicula, presupuesto_pelicula)
        elif opcion == "5":
            nombre_pelicula = input("Nombre de la pelicula a buscar: ")
            gestor_peliculas.buscar_pelicula(nombre_pelicula)
        elif opcion == "6":
            try:
                porcentaje = float(input("Introduce el porcentaje de aumento para los presupuestos: "))
                gestor_peliculas.modificar_presupuestos(porcentaje)
            except ValueError as e:
                print("El porcentaje no es un válido")
        else:
            print("Opción no valida")

if __name__ == "__main__":
    main()