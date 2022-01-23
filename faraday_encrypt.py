#####################################
#  ___                 _            #
# | __|_ _ _ _ __ _ __| |__ _ _  _  #
# | _/ _` | '_/ _` / _` / _` | || | #
# |_|\__,_|_| \__,_\__,_\__,_|\_, | #
# | __|_ _  __ _ _ _  _ _ __| |__/  #
# | _|| ' \/ _| '_| || | '_ \  _|   #
# |___|_||_\__|_|  \_, | .__/\__|   #
#                  |__/|_|          #
#####################################

# Faraday Encrypt
# Albert's first Faraday Industrial tool

from Crypto.Cipher import AES
import sys

def encrypt(data: str, key: str) -> str:
    """
    Encrypts the given input data using AES ECB encryption and a supplied key.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    # Pad the data to a multiple of 16 bytes
    data = data + b'\x00' * (16 - (len(data) % 16))
    return cipher.encrypt(data)

def encrypt_file(input_file: str, output_file: str, key: str) -> None:
    """
    Encrypts the contents of the given input file using AES ECB encryption and a supplied key.
    """
    with open(input_file, 'rb') as f:
        data = f.read()
    with open(output_file, 'wb') as f:
        f.write(encrypt(data, key))

if __name__ == "__main__":
    # Read the arguments of the program to get the key and list of files to encrypt
    key = sys.argv[1]
    files = sys.argv[2:]
    # Encrypt the files
    for file in files:
        encrypt_file(file, file + '.enc', key)
    # Print the encrypted files
    for file in files:
        print(file + '.enc')
