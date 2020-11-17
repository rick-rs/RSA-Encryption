import random

print(" = = = = = = RSA ENCRYPT V1.0 - BY: Henrique = = = = = = ")

def isPrime(val):
    for i in range(2, val):
        if val%i == 0:
            return False
    return True

def gcd(x, y): # Greatest Common Divisor
    while(y):
        x, y = y, x % y
    return x


def randomPrime(val): # Generate random prime numbers
    while True:
        x = random.randint(100, val)
        if isPrime(x):
            break
    return x

def findD(x): # Generate a random value for D
    d = random.randint(5, 20)
    while True:
        if (gcd(d,x) == 1 and isPrime(d)):
            return d
        d += 1

def findE(d, z): # Generate the value of E
    e = 1
    while True:
        if ( (e * d) % z == 1):
            return e
        e += 1

def generateKeys(): # Generate the global keys
    print("Generating keys...")
    global p, q, n, z, d, e
    p = randomPrime(random.randint(100,1000))
    q = randomPrime(random.randint(100,1000))
    n = p*q
    z = (p-1)*(q-1)
    d = findD(z)
    e = findE(d, z)

def listToString(stringList): # Convert list to string
    string = ""  
    for letter in stringList:  
        string += letter
    return string

def encrypt(text, e, n): # Encrypt each caractere and concat it
    print("Encrypting...")
    encrypted = []
    for letter in text:
        encrypted.append((ord(letter) ** e) % n) 
    return encrypted

def decrypt(text, d, n): # Decrypt each caractere and concat it
    print("Decrypting...")
    decrypted = []
    for letter in text:
        decrypted.append(chr(((letter) ** d) % n))
    return decrypted

# Take input
text = input("Insert a message: ")

# Key generation
p=0
q=0
n=0
z=0
d=0
e=0
generateKeys()

encryptedMessage = encrypt(text, e, n)
print("Encrypted message: " + str(encryptedMessage))
print("Public Key: ")
print("\tE: " + str(e))
print("Private Key: ")
print("\tD: " + str(d))
print("\tN: " + str(n))

decryptedMessage = decrypt(encryptedMessage, d, n)

print("Decrypted message: " + listToString(decryptedMessage))