# Transposition cipher
plaintext = str(input("Enter the msg: "))
key = int(input("Enter the key in single digit: "))

ciphertext = [''] * key
# print(ciphertext)


for col in range(key):
    pointer = col
    while pointer < len(plaintext):
        ciphertext[col] += plaintext[pointer]

        pointer += key
secret = ''.join(ciphertext)
print(secret)
leng = len(ciphertext[0])
result = [''] * leng


for col in range(leng):
    pointer = col
    while pointer < len(secret):
        result[col] += secret[pointer]
        pointer += leng

real = ''.join(result)
print(result)
print(real)
