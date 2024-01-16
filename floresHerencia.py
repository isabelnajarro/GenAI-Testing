from abc import ABC, abstractmethod

FLORESDISPONIBLES = ["Amapola", "Margarita"]

class Flor(ABC):
    def __init__(self, nombre, tipo, horasSol):
        self.nombre = nombre
        self.tipo = tipo
        self.horasSol = horasSol

    def darComida(self):
        print("La planta ha comido")

    @abstractmethod
    def cambiarTierra(self):
        pass

    @staticmethod
    def isAvailable(tipo):
        return tipo in FLORESDISPONIBLES

class Rosa(Flor):
    def __init__(self, nombre, tipo, horasSol, color):
        super().__init__(nombre, tipo, horasSol)
        self.color = color

    def darComida(self):
        print(f"Rosa de color {self.color} ha comido")
    
    def cambiarTierra(self):
        return self.horasSol > 2

class Amapola(Flor):
    def __init__(self, nombre, tipo, horasSol, temporada):
        super().__init__(nombre, tipo, horasSol)
        self.temporada = temporada

    def darComida(self):
        print(f"Amapola de temporada {self.temporada} ha comido")
    
    def cambiarTierra(self):
        return self.horasSol > 2


# Crear instancias de las subclases
rosa_azul = Rosa("Rosa", "Canina", 5, "Azul")
amapola_roja = Amapola("Amapola", "Oriental", 3, "Verano")

# Llamar a los métodos de las subclases
print("Resultado a si se le puede cambiar la tierra (Rosa): ", rosa_azul.cambiarTierra())
print("¿Está disponible? (Rosa): ", rosa_azul.isAvailable(rosa_azul.tipo))

print("Resultado a si se le puede cambiar la tierra (Amapola): ", amapola_roja.cambiarTierra())
print("¿Está disponible? (Amapola): ", amapola_roja.isAvailable(amapola_roja.tipo))
