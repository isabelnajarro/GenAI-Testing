from abc import ABC, abstractmethod

class Flor:
    def __init__(self, nombre, tipo, horasSol):
        self.nombre = nombre
        self.tipo = tipo
        self.horasSol = horasSol

    def darComida(self):
        print("La planta ha comido")

    @staticmethod
    def mensaje_static():
        print("Este es un método estático en la clase Flor")

    @abstractmethod
    def cambiarTierra(self):
        pass

class Rosa(Flor):
    def __init__(self, nombre, tipo, horasSol, color):
        super().__init__(nombre, tipo, horasSol)
        self.color = color

    def darComida(self):
        print("Rosa de color {} ha comido".format(self.color))


class Amapola(Flor):
    def __init__(self, nombre, tipo, horasSol, temporada):
        super().__init__(nombre, tipo, horasSol)
        self.temporada = temporada

    def darComida(self):
        print("Amapola de temporada {} ha comido".format(self.temporada))


flor_verde = Flor("Planta", "Verde", 2)
flor_verde.darComida()

rosa_azul = Rosa("Rosa", "Canina", 5, "Azul")
rosa_azul.darComida()

amapola_roja = Amapola("Amapola", "Oriental", 3, "Verano")
amapola_roja.darComida()

print("Metodo estático y abstracto")
Flor.mensaje_static()