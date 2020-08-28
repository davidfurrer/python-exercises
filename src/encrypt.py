from cryptography.fernet import Fernet

file = open("solutions.key", "rb")  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()

# ToDo make args
input_file = "01_hello/solutions/hello.py"
output_file = "01_hello/solutions/hello.encrypted"

with open(input_file, "rb") as f:
    data = f.read()  # Read the bytes of the input file

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, "wb") as f:
    f.write(encrypted)  # Write the encrypted bytes to the output file

# Note: You can delete input_file here if you want

# ref.: https://nitratine.net/blog/post/encryption-and-decryption-in-python/
