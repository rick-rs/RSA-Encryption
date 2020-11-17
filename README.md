
# RSA-Encryption V1.0
    In this encryption system, the encryption key is public and is different from the decryption key that is secret.
## How it works
    1. Firstly we generate two random primes that we call "P" and "Q".
    2. Next, two new numbers "N" and "Z" are calculated according to with the chosen "P" and "Q" numbers. (N = P * Q) and  (Z = (P - 1) * (Q - 1)).
    3. "D" is a random prime number whose GCD (Great Common Divisor) in relation to "Z" must be equal to 1.
    4. For the value of "E" we must satisfy the following condition: (E * D) mod Z = 1
    5. Finally, to encrypt we have to take each carachter of the text and apply this formula: (EncryptedText = (OriginalText ^ E) mod N). The "E" is the public key and the "N" and "D" are the private keys.
    6. To decrypt the word we apply this: (OriginalText = (EncryptedText ^ D) mod N)
## Running the code

Open the terminal and run
```bash
	$ python main.py
```

## Meta

Henrique Ribeiro – [@Henrique-R-S](https://github.com/Henrique-R-S)
 
