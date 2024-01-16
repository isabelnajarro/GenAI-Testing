# Lista de temperaturas en grados Celsius
temperaturas = [-150, -140, -130, -160, -145, -135, -125]

# Temperatura crítica del nitrógeno
temperatura_critica = -147

# Filtrar temperaturas por encima de la temperatura crítica utilizando lista por comprensión
temperaturas_gaseosas = [temp for temp in temperaturas if temp > temperatura_critica]

# Imprimir las temperaturas gaseosas
print("Temperaturas en las que el nitrógeno permanece en estado gaseoso:")
print(temperaturas_gaseosas)