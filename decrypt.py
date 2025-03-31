from cryptography.fernet import Fernet
import os

# Cargo en, modo binario, la clabe de un cifrado del archivo 'key.key' 
# y posteriormente devuelvo en contenido en modo de bytes.
def load_key():
    return open('key.key', 'rb').read()


def decrypt(items, key):
    f = Fernet(key)
    # Itero cada archvio a desencriptar
    for item in items:  
        # Verifico que el elemento se un archivo
        if os.path.isfile(item):
            with open(item, 'rb') as file:
                encrypted_data = file.read()
            # utilizo la clave de cifrado para desencriptar los datos
            decrypt_data = f.decrypt(encrypted_data)
            with open(item, 'wb') as file:
                # Sobreescribo los datos cifrados con los desencriptados
                file.write(decrypt_data)

if __name__ == '__main__':
    # Ubicacion del archivo cifrado
    path_to_decrypt = 'C:\\Developer\\Pentest\\victima'
    # Elimino el archivo 'rescate.txt'
    os.remove(path_to_decrypt+'\\'+'rescate.txt')
    # Lista en la ubicacion del archivo cifrado
    items = os.listdir(path_to_decrypt)

    full_path = [path_to_decrypt+'\\'+ item for item in items]

    key = load_key()
    # Llamo a la funcion pasando la lista de archivo y la clave de cifrado
    decrypt(full_path, key)


# Bibliotecas:
    # Cryptography: Cifrado y descifrado de datos usando algoritmos de datos,
        # en este caso, simetricos a Fernet.
    # Os: Permite realizar operaciones con el sistema operativo, como manipulacion
        # de archivos y directorios.