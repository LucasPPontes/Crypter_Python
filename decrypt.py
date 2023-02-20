from cryptography.fernet import Fernet

with open("yourKey.key", "rb") as keyfile:
    key = keyfile.read()

f = Fernet((key))

with open("fileteste.csv", "rb") as crypted_file:
    crypted = crypted_file.read()

decrypted = f.decrypt(crypted)

with open("fileteste_decrypt.csv", "wb") as dec_file:
    dec_file.write(decrypted)