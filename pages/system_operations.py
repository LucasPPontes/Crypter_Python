from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("yourKey.key","wb") as yourkey:
        yourkey.write(key)

def crypt():
    with open("yourKey.key", "rb") as keyfile:
        key = keyfile.read()

    f = Fernet((key))

    try:
        with open("fileteste.csv", "rb") as original_file:
            original = original_file.read()

        encrypt_file = f.encrypt(original)

        with open("fileteste.csv","wb") as cripted_file:
            cripted_file.write(encrypt_file)

    except Exception as e:
        print(e)

def decrypt():
    with open("yourKey.key", "rb") as keyfile:
        key = keyfile.read()

    f = Fernet((key))
    try:

        with open("fileteste.csv", "rb") as crypted_file:
            crypted = crypted_file.read()

        decrypted = f.decrypt(crypted)

        with open("fileteste_decrypt.csv", "wb") as dec_file:
            dec_file.write(decrypted)
    
    except Exception as e:
        print(e)

