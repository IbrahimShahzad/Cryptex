import argparse
from cryptography.fernet import Fernet

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key(filename):
    """
    Loads the key from the current directory named `key.key`
    """
    return open(filename, "rb").read()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

    # encrypt
    encrypted_data = f.encrypt(file_data)

    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def check_valid_arguments(args):
    if args.encrypt and args.decrypt:
        print("Conflicting Arguments parsed!")
        exit()
    if args.encrypt:
        if args.file == None:
            print("File required for encryption!")
            exit()
        if args.key == None:
            print("Key required for encryption!")
            exit()
        return "encrypt"
    if args.decrypt:
        if args.file == None:
            print("File required for encryption!")
            exit()
        if args.key == None:
            print("Key required for encryption!")
            exit()
        return "decrypt"
    if args.generate_key:
        return "generate_key"
    if args.load_key:
        return "load_key"

def main():
    # Construct the argument parser
    ap = argparse.ArgumentParser(description="Encrypt/Decrypt 'file' with 'key'")

    # Add the arguments to the parser
    ap.add_argument("-f","--file", help="The file you want to encrypt or decrypt")
    ap.add_argument("-k","--key", help="The key you want to encrypt or decrypt with")
    ap.add_argument("-e","--encrypt", help="encrypt", action="store_true")
    ap.add_argument("-d","--decrypt", help="decrypt", action="store_true")
    ap.add_argument("-g","--generate-key", help="generate key file", action="store_true")
    ap.add_argument("-l","--load-key", help="load and print key file")
    args = ap.parse_args()
    action = check_valid_arguments(args)
    if action == "generate_key":
        write_key()
    if action == "load_key":
        print(load_key(args.load_key))
    if action == "encrypt":
        encrypt(args.file,load_key(args.key))
    if action == "decrypt":
        decrypt(args.file,load_key(args.key))

if __name__ == "__main__":
    main()