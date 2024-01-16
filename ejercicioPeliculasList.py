# Ejemplo de códigos ANSI para diferentes colores
COLOR_ROJO = "\033[91m"
COLOR_VERDE = "\033[92m"
COLOR_AZUL = "\033[94m"
COLOR_AMARILLO = "\033[93m"
COLOR_NARANJA = "\033[38;5;208m"  # Código ANSI para naranja
COLOR_MORADO = "\033[95m"         # Código ANSI para morado claro
RESET_COLOR = "\033[0m"  # Para resetear el color a su valor por defecto

print(COLOR_VERDE + "1. Añadir pelicula"  + RESET_COLOR)

class Gestionpeliculas:
    def __init__(self):
        self.peliculas = []

    def añadir_pelicula(self, pelicula):
        if pelicula not in self.peliculas:
            self.peliculas.append(pelicula)
            print(f'pelicula "{pelicula}" añadida a la lista.')
        else:
            print(f'La pelicula "{pelicula}" ya está en la lista.')

    def eliminar_pelicula(self, pelicula):
        if pelicula in self.peliculas:
            self.peliculas.remove(pelicula)
            print(f'pelicula "{pelicula}" eliminada de la lista.')
        else:
            print(f'La pelicula "{pelicula}" no está en la lista.')

    def mostrar_peliculas(self):
        for pelicula in self.peliculas:
            print(pelicula)

    def buscar_pelicula(self, pelicula):
        if pelicula in self.peliculas:
            print(f'La pelicula está en la lista.')
        else:
            print(f'La pelicula no está en la lista.')

# Función principal
def main():
    gestor_peliculas = Gestionpeliculas()

    while True:
        print("\nMenu:")
        print("1. Añadir pelicula")
        print("2. Eliminar pelicula")
        print("3. Mostrar Lista de peliculas")
        print("4. Buscar pelicula")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_pelicula = input("Introduce el nombre de la pelicula que deseas añadir: ")
            gestor_peliculas.añadir_pelicula(nombre_pelicula)
        elif opcion == "2":
            nombre_pelicula = input("Introduce el nombre de la pelicula que deseas eliminar: ")
            gestor_peliculas.eliminar_pelicula(nombre_pelicula)
        elif opcion == "3":
            gestor_peliculas.mostrar_peliculas()
        elif opcion == "4":
            nombre_pelicula = input("Introduce el nombre de la pelicula que deseas buscar: ")
            gestor_peliculas.buscar_pelicula(nombre_pelicula)
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()