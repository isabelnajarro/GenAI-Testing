from datetime import datetime

print(datetime.now())

nacimiento = datetime(1998, 8, 11)

print("Fecha nacimiento")
print(nacimiento.day)
print(nacimiento.month)
print(nacimiento.year)

def obtener_dia(num):
    switch = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }

print("Dia de la semana que naci, teniendo en cuenta que se empieza en 0: ", nacimiento.weekday())
nombre_dia = obtener_dia(nacimiento.weekday())
print("Naci un: ", nombre_dia)

diferencia = datetime.now() - nacimiento
print("Han pasado {} dias desde mi nacimiento".format(diferencia))
