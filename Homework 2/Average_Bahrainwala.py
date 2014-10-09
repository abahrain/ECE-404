"""
Homework Number: 2
Name: Adam Bahrainwala
ECN Login:abahrain
Due Date: 30/1/2014
"""
import sys
import DES_Bahrainwala
import BitVector

# runs the encryption twice and compares the outputs to count the number of differences
def confuse(rkey,way,rnd,fle):
    alpha=DES_Bahrainwala.crypt(rkey,way,rnd,fle)
    rkey= rkey | 10000000000000000000000000000000000000000000000000000000
    beta=DES_Bahrainwala.crypt(rkey,way,rnd,fle)
    return sum(i != j for i, j in zip(alpha, beta))

# runs the encryption twice and compares the outputs to count the number of differences
def diffuse(rkey,way,rnd,fle):
    alpha=DES_Bahrainwala.crypt(rkey,way,rnd,fle)
    fle= fle | 10000000000000000000000000000000000000000000000000000000
    beta=DES_Bahrainwala.crypt(rkey,way,rnd,fle)
    return sum(i != j for i, j in zip(alpha, beta))

# main
fle=raw_input("Enter file name: ")
mode=raw_input("Enter mode <encrypt or decrypt>: ")
round_key = DES_Bahrainwala.get_encryption_key()
if mode == "encrypt" or mode == "decrypt":
    for i in range(0,16):
        c=confuse(round_key,mode,i,fle)
        d=diffuse(round_key,mode,i,fle)
    print "Confussion average" + c
    print "Diffusion average" + d
else:
    print("Invalid input. <encrypt or decrypt>")