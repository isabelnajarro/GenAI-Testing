import hashlib
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class AnonimizadorCifrador:
    def __init__(self):
        self.salt = os.environ.get("SALT", "default_salt").encode()

    def hash_con_salt(self, nombre, apellido):
        nombre_completo = nombre + " " + apellido
        nombre_completo_codificado = nombre_completo.encode()
        # Combinar el nombre completo codificado con el salt
        entrada_con_salt = nombre_completo_codificado + self.salt
        # Crear el hash
        hash_objeto = hashlib.sha256(entrada_con_salt)
        hash_hex = hash_objeto.hexdigest()
        return hash_hex
# ...............................................................................................................................
    
    def generar_clave(self):
        return Fernet.generate_key()

    def cifrar_nombre(self, nombre, clave):
        # Crear una instancia de Fernet con la clave proporcionada
        f = Fernet(clave)
        # Codificar el nombre y cifrarlo
        nombre_codificado = nombre.encode()
        nombre_cifrado = f.encrypt(nombre_codificado)
        return nombre_cifrado
    
    def descifrar_nombre(self, nombre_cifrado, clave):
        # Crear una instancia de Fernet con la clave proporcionada
        f = Fernet(clave)
        # Descifrar y decodificar el nombre
        nombre_descifrado = f.decrypt(nombre_cifrado)
        nombre_original = nombre_descifrado.decode()
        return nombre_original

# ...............................................................................................................................

    def generar_par_claves(self):
        clave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        clave_publica = clave_privada.public_key()
        return clave_publica, clave_privada

    def cifrar_nombre_asimetrico(self, nombre, clave_publica):
        nombre_codificado = nombre.encode()
        nombre_cifrado = clave_publica.encrypt(
        nombre_codificado,
        padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None))
        return nombre_cifrado
    
    def descifrar_nombre_asimetrico(self, nombre_cifrado, clave_privada):
        nombre_descifrado = clave_privada.decrypt(
        nombre_cifrado, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),label=None))
        return nombre_descifrado.decode()


if __name__ == "__main__":
    anon_cifrador = AnonimizadorCifrador()
    nombre_anonimizado = anon_cifrador.hash_con_salt("Isabel", "Najarro")
    print(f"Nombre anonimizado: {nombre_anonimizado}")

    # Fernet - simetrico
    clave = anon_cifrador.generar_clave()
    nombre_cifrado_sim = anon_cifrador.cifrar_nombre("Isabel Najarro", clave)
    print("Nombre Cifrado:", nombre_cifrado_sim)
    nombre_descifrado = anon_cifrador.descifrar_nombre(nombre_cifrado_sim, clave)
    print("Nombre Descifrado:", nombre_descifrado)

    # Cifrado asimetrico
    clave_publica, clave_privada = anon_cifrador.generar_par_claves()
    nombre_cifrado_asim = anon_cifrador.cifrar_nombre_asimetrico("Isabel Najarro", clave_publica)
    print("Nombre Cifrado:", nombre_cifrado_asim)
    nombre_descifrado = anon_cifrador.descifrar_nombre_asimetrico(nombre_cifrado_asim, clave_privada)
    print("Nombre Descifrado:", nombre_descifrado)



