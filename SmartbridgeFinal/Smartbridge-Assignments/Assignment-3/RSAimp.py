# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:02:23 2023

@author: Adhithya
"""

import math

def modinv(a,m):
    for x in range(1,m):
        if(((a%m) * (x%m)) % m == 1):
            return x
    return -1


p = int(input("Enter the value of p(must be a prime number): "))
q = int(input("Enter the value of q(must be a prime number): "))
n = p*q
print("n = ",n)
totient = (p-1)*(q-1)
print("Totient = ",totient)

print("\nAll possible Public keys and Private keys\n")
for a in range(2,totient):
    if(math.gcd(a,totient) == 1):
        print("Encryption key(e,n) = ",(a,n),"  <---->  Decryption key(d,n) = ",(modinv(a,totient),n)) 
    
e = int(input("Choose a value for e from the above for encryption: "));

message = input("Enter the message: ").upper()

    
print("\nThe Encrypted message in a sequence of numbers: ")
for ch in message:
    x = (((ord(ch)-65)**e) % n)
    print(x)

    
d = modinv(e,totient)
decrypt = ""
print("\nDecryption:")
for ch in message:
     x = (((ord(ch)-65)**e) % n)
     y = ((x**d) % n) % n
     print(x,"-->",y,"-->",chr(y%26 +65))
     decrypt += chr(y%26 +65)
print("\nThe Decrypted message is: ",decrypt)