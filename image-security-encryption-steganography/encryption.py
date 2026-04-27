import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


def encrypt(key, filename):
    chunksize = 64 * 1024
    output_file = "(encry)" + filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    iv = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, iv)

    with open(filename, "rb") as infile:
        with open(output_file, "wb") as outfile:
            outfile.write(filesize.encode("utf-8"))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                if len(chunk) % 16 != 0:
                    chunk += b" " * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))

    print("Encrypted file created:", output_file)


def decrypt(key, filename):
    chunksize = 64 * 1024

    # Removes the prefix "(encry)" from the encrypted file name
    output_file = filename[7:] if filename.startswith("(encry)") else "decrypted_" + filename

    with open(filename, "rb") as infile:
        filesize = int(infile.read(16))
        iv = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(output_file, "wb") as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(filesize)

    print("Decrypted file created:", output_file)


def getKey(password):
    hasher = SHA256.new(password.encode("utf-8"))
    return hasher.digest()


def Main():
    choice = input("Would you like to (E) encrypt or (D) decrypt? ")

    if choice in ["E", "e"]:
        filename = input("File to encrypt: ")
        password = input("Password: ")
        encrypt(getKey(password), filename)
        print("Done")

    elif choice in ["D", "d"]:
        filename = input("File to decrypt: ")
        password = input("Password: ")
        decrypt(getKey(password), filename)
        print("Done")

    else:
        print("No option selected, closing...")


if __name__ == "__main__":
    Main()
