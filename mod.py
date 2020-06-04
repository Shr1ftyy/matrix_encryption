#!C:/Users/Syeam/AppData/Local/Programs/Python/Python37/python.exe
import numpy as np 
import math
import sys


# Function for finding the modular inverse of a, given mod m
def modInverse(a, m) : 
    # Checks if ax mod m = 1, if yes then it returns x since it is the modular inverse
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            # print(f"({a} * {x}) % {m}")
            return x 
    return 1
  
# Alphabet - 90 characters
alphabet="!ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789@#$%^&()-+<>?/\|{}[]`~,.;:' "
print(len(alphabet))

# Get input from user and matrix
message = input("Insert Message Here:\n>")
orgLen = len(message)
print(len(message))

# Checks if all the characters in the message are also in the alphabet
for i in message:
    if i not in alphabet:
        raise TypeError("The character '" +str(i) + "' is not in the provided alphabet" )

# Checks if the length of the message is even, if not the program halts
if len(message) % 2 != 0:
    message += stopChar

# Asks user for encoding matrix
encode = input("Insert 2x2 encoding matrix below:\n>").split(",")
encode = [int(i) for i in encode]

#Checks if the input contained 4 elements, as a 2x2 matrix has 4 elements
if len(encode) != 4:
    raise ValueError("You must include 4 numbers in the encoding matrix")

# Encoding Matrix
# Converts user input into an 2x2 matrix
encode = np.int32(np.array(encode).reshape((2,2)))
print(encode.shape)

# Converts input message into pairs of vectors
en_message = [alphabet.index(i) for i in message]
en_message = np.array(en_message).reshape((int(len(message)/2), 2))
print("Vector form of sentence")
print(en_message)

# Finds determinent of the encoding matrix
det = np.round(np.linalg.det(encode), 4)


# Checks if the determinent of the matrix is divisble, if so the program halts
if len(alphabet) % det == 0:
    raise ValueError(f"The length of the alphabet: {len(alphabet)} must\n"
                    f"not be divisible by the determinant of the encoding matrix\n" 
                    f"Determinant of given matrix: {det}")

# Checks if the determinent of the matrix's modular inverse is 1 or 0, if so the program halts
if (modInverse(det, len(alphabet)) == 1) or (modInverse(det, len(alphabet)) == 0):
    raise ValueError("The modular inverse of the determinant of the coding matrix "
                    "cannot be 0 or 1")

# Encoded message
encoded = np.array([])
en =  ''

# Encoding
for c in en_message:
    encoded = np.int32(np.append(encoded, np.dot(encode,c))) % len(alphabet)

for d in encoded:
    en += alphabet[d]

print(f"Encoding Matrix:\n{encode}")
print(f"Encoded Message: ")
encoded = encoded.reshape((int(len(encoded)/2),2))
print(en)
print(encoded)

# Decoding
decipher = (modInverse(det, len(alphabet)) * np.array([[encode[1,1],-1*encode[0,1]],[-1*encode[1,0],encode[0,0]]])) % len(alphabet)
print("Deciphering Matrix:")
print(decipher)
decoded = ''

# Converts decoded row vector into character format
for i in range(0,int(len(message)/2)):
    enc = np.expand_dims(encoded[i], axis=1)
    dec = np.dot(decipher, enc)
    for j in dec:
        j = int(j[0])
        decoded += alphabet[j%len(alphabet)]

# Removes stop character if there was any
if orgLen % 2 != 0:
    decoded = decoded[:-1]

# Print decoded message
print(decoded)

