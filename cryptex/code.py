import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os



def gen_key():
    key = Fernet.generate_key()

    with open('key.key','wb') as f:
        f.write(key)
    print(key)

def read_key():
    with open('key.key','rb') as f:
        key = f.read()
        return key

if __name__ == '__main__':
    gen_key() 
    backend = default_backend()
    iv = os.urandom(16)
    key = read_key()
    cipher = Cipher(algorithms.AES(key),modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(b"a secret message") + encryptor.finalize()
    decryptor = cipher.decryptor()
    decryptor.update(ct) + decryptor.finalize()
    print(read_key())
