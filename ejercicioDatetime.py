from datetime import datetime

print(datetime.now())

nacimiento = datetime(1998, 8, 11)

print("Fecha nacimiento")
print(nacimiento.day)
print(nacimiento.month)
print(nacimiento.year)

print("Dia de la semana que naci, teniendo en cuenta que se empieza en 0: ", nacimiento.weekday())
nombre_dia = nacimiento.strftime('%A')
print("Naci un: ", nombre_dia)

diferencia = datetime.now() - nacimiento
print("Han pasado {} dias desde mi nacimiento".format(diferencia))
