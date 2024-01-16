
mi_tupla = (1,2,3)
try:
    mi_tupla[0] = 4
except TypeError as e:
    print(f"Error: {e}")

tupla_mixta = (1, "dos", [3, 4], {5: "cinco"}, (6, 7), 8.0, True, None, {9})

tupla_list = list(tupla_mixta)
print(tupla_list)

# Crear una nueva lista con el primer elemento modificado
tupla_list[1] = 2
tupla_modificada = tuple(tupla_list)
print("tupla modificada", tupla_modificada)

# OPERACIONES NUMERICAS
tupla_numerica = (5, 3, 8, 12, 6)

# Operaciones de suma, máximo y mínimo
suma = sum(tupla_numerica)
maximo = max(tupla_numerica)
minimo = min(tupla_numerica)

# Imprimir los resultados
print(f"Suma: {suma}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

# calcular los cuadradros
cuadrados = [x**2 for x in tupla_numerica]
print("Cuadrados:", cuadrados)

# desempaquetar la tupla
var1, var2, var3, var4, var5 = tupla_numerica
print("Desempaquetado:", var1, var2, var3, var4, var5)
