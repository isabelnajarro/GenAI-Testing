from abc import ABC, abstractmethod

FLORESDISPONIBLES = ["Amapola", "Margarita"]


class Flor:
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
    def isAvailable(type):
        return type in FLORESDISPONIBLES

class Rosa(Flor):
    def __init__(self, nombre, tipo, horasSol, color):
        super().__init__(nombre, tipo, horasSol)
        self.color = color

    def darComida(self):
        print("Rosa de color {} ha comido".format(self.color))
    
    def cambiar_tierra(self):
        return self.horasSol > 2


class Amapola(Flor):
    def __init__(self, nombre, tipo, horasSol, temporada):
        super().__init__(nombre, tipo, horasSol)
        self.temporada = temporada

    def darComida(self):
        print("Amapola de temporada {} ha comido".format(self.temporada))
    
    def cambiar_tierra(self):
        return self.horasSol > 2


flor_verde = Flor("Planta", "Verde", 2)
flor_verde.darComida()
print("Resultado a si se le puede cambiar la tierra: ", flor_verde.cambiarTierra())
print("¿Está disponible? ", flor_verde.isAvailable(flor_verde.tipo))

rosa_azul = Rosa("Rosa", "Canina", 5, "Azul")
rosa_azul.darComida()
print("Resultado a si se le puede cambiar la tierra: ", rosa_azul.cambiarTierra())
print("¿Está disponible? ", rosa_azul.isAvailable(rosa_azul.tipo))


amapola_roja = Amapola("Amapola", "Oriental", 3, "Verano")
amapola_roja.darComida()
print("Resultado a si se le puede cambiar la tierra: ",amapola_roja.cambiarTierra())
print("¿Está disponible? ", amapola_roja.isAvailable(amapola_roja.tipo))

