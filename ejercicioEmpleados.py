import copy

empleados = [
    ["Pedro", ["Python", "SQL"]],
    ["Manolo", ["Java", "C++", "JavaScript"]],
    ["Alejandro", ["HTML", "CSS", "JavaScript"]]
    ]
print("Original: ", empleados)

# Copia superficial usando .copy()
copia_superficial = empleados.copy()
print("Copia superficial: ", copia_superficial)

# Copia profunda usando deepcopy()
copia_profunda = copy.deepcopy(empleados)
print("Copia profunda: ", copia_profunda)

# Ejercicio 3: poner a Pedro una nueva habilidad
[empleado[1].append("Mongo") for empleado in empleados if empleado[0] == "Pedro"]
print("\n---- EJERCICIO 3 ------")
print("original: ", empleados)
print("Copia superficial: ", copia_superficial)
print("Copia profunda: ", copia_profunda)

# Ejercicio 4 añadir con indice negativo java a Alejandro
copia_profunda[-1][1].append("Java")

# Ejercicio 5
nuevo_empleado = ["Juan", ["Node.js", "redis"]]
copia_profunda.append(nuevo_empleado)

# Comparar si devuelve lo mismo
resultado_esperado = [
["Pedro", ["Python", "SQL"]],
["Manolo", ["Java", "C++", "JavaScript"]],
["Alejandro", ["HTML", "CSS", "JavaScript","Java"]],
["Juan", ["Node.js", "redis"]]
]

if copia_profunda == resultado_esperado:
    print("Las listas son iguales.")
else:
    print("Las listas son diferentes.")