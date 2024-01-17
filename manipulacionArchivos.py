fichero = "mi_archivo.txt"

try:
    with open(fichero, "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encontró. Creando el archivo...")
    with open(fichero, "w") as archivo:
        archivo.write("ABCDEFGHIKLMNO\n")
        archivo.write("1234567890\n")
        archivo.write("+-*/\n")
        archivo.write(".,:;-_\n")
        archivo.write("PQRSTUVWXYZ\n")
    print("Archivo creado")

with open(fichero, 'r', encoding='UTF8') as archivo:
    linea = archivo.readline()
    posicion_inicial = archivo.seek(0)
    while linea:
        print(linea.strip())
        pos = archivo.tell()
        print("Posición del cursor: ", pos)
        linea = archivo.readline()

with open(fichero, "r") as archivo_lectura:
    contenido = archivo_lectura.read()
with open(fichero, "w") as archivo_escritura:
    archivo_escritura.write(contenido)
    archivo_escritura.write("AaEeIiOoUu")

with open(fichero, "a+") as archivo_anexar:
    archivo_anexar.seek(0)
    contenido = archivo_anexar.read()
    print("\nContenido completo después de anexar:", contenido)

try:
    with open(fichero, "a") as archivo_error:
        pass
except Exception as e:
    print("\nError al abrir en modo 'a':", e)
    print("Explicación: 'a' solo permite escritura al final del archivo, no lectura.")
