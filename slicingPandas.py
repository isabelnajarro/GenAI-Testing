import pandas as pd

serie_temperaturas = pd.Series([25, 28, 24, 26, 29, 23, 27], name="Temperaturas")
serie_precipitacion = pd.Series([10, 5, 15, 8, 12, 7, 10], name="Precipitación")

slicing_temperaturas = serie_temperaturas[1:4]
print("Slicing temperaturas: ", slicing_temperaturas)  
slicing_precipitacion = serie_precipitacion[::2] 
print("Slicing precipitacion: ", slicing_precipitacion) 

temp_prec = pd.concat([slicing_temperaturas, slicing_precipitacion], axis=1)
print("Resultado fusion: ", temp_prec)

print("Operaciones aritméticas: ")
suma = temp_prec + 2
print("Suma: ", suma)
resta = temp_prec - 2 
print("Resta: ", resta)
multiplicacion = temp_prec * 2
print("Multiplicacion: ", multiplicacion)
division = temp_prec / 2
print("Division: ", division)
