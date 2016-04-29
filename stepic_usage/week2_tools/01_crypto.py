import simplecrypt  # import encrypt, decrypt
#import pycrypto

print('-----START-----')

with open('module2\encrypted.bin', 'rb') as inp:
    text = inp.read().rstrip()

print(text)
with open('module2\passwords.txt', 'r') as passwords:
    for line in passwords:
        password = line.strip()
        print(password)
        try:
            plaintext = simplecrypt.decrypt(password, text)
            print(plaintext)
        except simplecrypt.DecryptionException:
            print('DecryptionException')

