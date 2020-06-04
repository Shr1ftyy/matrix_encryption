#!C:/Users/Syeam/AppData/Local/Programs/Python/Python37/python.exe
import numpy as np 
import math
import sys

# Alphabet - 90 characters
alphabet="!ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789@#$%^&()-+<>?/\|{}[]`~,.;:' "

# Function for finding the modular inverse of a, given mod m
def modInverse(a, m) : 
    # Checks if ax mod m = 1, if yes then it returns x since it is the modular inverse
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            # print(f"({a} * {x}) % {m}")
            return x 
    return 1

# Get input from user and matrix
message = input("Insert Message Here: ")
print(f"length: {len(message)}")

# Checks if all the characters in the message are also in the alphabet
for i in message:
    if i not in alphabet:
        raise TypeError("The character '" +str(i) + "' is not in the provided alphabet" )

# Asks user for encoding matrix
encode = input("Insert Values for matrix (e.g 1,1,2,3 for [[1,1], [2,3]])\n>").split(",")
encode = [int(i) for i in encode]

# Encoding Matrix
# Converts user input into an nxn matrix
try:
    encode = np.int32(np.array(encode).reshape(-1, len(message)))
    print(encode)
    print(encode.shape)
except:
    print("The shaped of the square encoding matrix does not match the length of the message")
    sys.exit()

# Converts input message into column vector
en_message = [alphabet.index(i) for i in message]
en_message = np.array(en_message).reshape(-1, 1)

# Finds determinent of the encoding matrix
det = round(np.linalg.det(encode), 4)

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
en_message = (np.dot(encode,en_message))
print("Encoded Matrix")
print(en_message)

# Shows encoded message
en = ''

for i in en_message:
    en += alphabet[int(i%len(alphabet))]

print("Encoded Message:")
print(en)


# Asks user if they would like to save the encoded message
save_en = input("Would you like to save the encoded message (y/n)?\n").lower().strip()

# Checks if user said yes, otherwise the program skips saving the encoded message
if save_en == "y":
    print("Saving Message")
    f = open("encoded.txt","w")
    f.write(en)
    f.close()
    print("Saved Message")
else:
    ("Skipping save...")

# Decoding

# Finds dot product between the inverse of the encoding matrix and the encoding message 
dec = (np.dot(np.linalg.inv(encode), en_message))
print("dec:")
print(dec)

text = ""

# Converts the values to the its corresponding characters in the alphabet
for i in dec:
    for char in i:
        print(alphabet[int(char)])
        # text += chr(int(char)+64)
        text += alphabet[int(char)]

# Print decoded message
print(text)

