import argparse
from cryptography.fernet import Fernet, InvalidToken


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument("-k", "--key", metavar="key", help="key to decrypt solution")
    return parser.parse_args()


# file = open("solutions.key", "rb")  # Open the file as wb to read bytes
# key = file.read()  # The key will be type bytes
# file.close()

args = get_args()
key = args.key

input_file = "01_hello/solutions/hello.encrypted"
output_file = "01_hello/solutions/hello_test.py"


with open(input_file, "rb") as f:
    data = f.read()  # Read the bytes of the encrypted file

fernet = Fernet(key)
try:
    decrypted = fernet.decrypt(data)

    with open(output_file, "wb") as f:
        f.write(decrypted)  # Write the decrypted bytes to the output file

    # Note: You can delete input_file here if you want
except InvalidToken as e:
    print("Invalid Key - Unsuccessfully decrypted")
