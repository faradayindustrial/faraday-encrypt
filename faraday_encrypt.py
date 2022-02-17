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

import sys
from itertools import cycle

def encrypt(data: bytes, key: bytes) -> str:
    """
    Encrypts the given input data using XOR and a supplied key.
    """
    return bytes(x ^ y for x, y in zip(data, cycle(key)))

def encrypt_file(input_file: str, output_file: str, key: str) -> None:
    """
    Encrypts the contents of the given input file using XOR encryption and a supplied key.
    """
    with open(input_file, 'rb') as f:
        data = f.read()
    with open(output_file, 'wb') as f:
        f.write(encrypt(data, key))

if __name__ == "__main__":
    # Read the arguments of the program to get the key and list of files to encrypt
    key = sys.argv[1].encode()
    files = sys.argv[2:]
    # Encrypt the files
    for file in files:
        encrypt_file(file, file + '.enc', key)
    # Print the encrypted files
    for file in files:
        print(file + '.enc')
