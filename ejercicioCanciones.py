import random

canciones = ['Canción1', 'Canción2', 'Canción3', 'Canción4', 'Canción5']
duraciones = [3.5, 4.2, 3.8, 5.1, 4.5]

canciones_dict = dict(zip(canciones, duraciones))
print("Diccionario combinado:")
print(canciones_dict)

# las 3 canciones más largas
canciones_largas = dict(sorted(canciones_dict.items(), key=lambda x: x[1], reverse=True)[:3])
print("Las 3 canciones más largas: ", canciones_largas)

# Diccionario con canciones aleatorias
canciones_dict = dict(random.sample(canciones_dict.items(), k=2))
print("Diccionario con canciones aleatorias: ", canciones_dict)