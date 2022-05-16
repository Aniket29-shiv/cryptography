# Transposition cipher
plaintext = str(input("Enter the msg: "))
key = int(input("Enter the key in single digit: "))

def pad(text):
    while len(text) % key != 0:
        text += " "
    return text

plaintext = pad(plaintext)

ciphertext = ['']*key

for column in range(key):
    pointer = column 
    while pointer<len(plaintext):
        ciphertext[column] += plaintext[pointer]
        pointer += key

secret = ''.join(ciphertext)
print("Encryption: ",secret)

plain = ['']*key
key2 = len(ciphertext[0])

for column in range(key2):
    pointer = column
    while pointer<len(secret):
        plain[column] += secret[pointer]
        pointer += key2

result = ''.join(plain)

print("Decryption: ",result)