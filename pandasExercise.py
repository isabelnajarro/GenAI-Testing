import pandas as pd 

numeros = [1,2,3,4,5]
serie = pd.Series(numeros)
print("Serie: ", serie)

nuevo = 10
serie = serie.append(pd.Series([nuevo]))
print("Serie: ", serie)

indice = 3
serie = serie.drop(indice)
print("Serie: ", serie)

print("Operaciones aritméticas: ")
suma = serie + 2
print("Suma: ", suma)
resta = serie - 2 
print("Resta: ", resta)
multiplicacion = serie * 2
print("Multiplicacion: ", multiplicacion)
division = serie / 2
print("Division: ", division)
