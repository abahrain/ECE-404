#!/usr/bin/env python

##Homework Number: 6
##Name: Adam Bahrainwala
##ECN Login: abahrain
##Due Date: 06/03/2014

import sys
from BitVector import *
import math
from PrimeGenerator import *

def prime_gen(e): ## compute the p and q values. Test that those are valid values.
    generator = PrimeGenerator( bits = 32, debug = 0 )
    p = generator.findPrime()
    q = generator.findPrime()
    if p==q: ##test 1
    	p,q = prime_gen(e)
    	return p,q
    tempp = p
    tempq = q
    test1 = 0
    test2 = 0
    while(tempp > 0 & tempq > 0): ##test2
        if tempp == 3:
            test1 = 1
        if tempq == 3:
          test2 = 1
        tempp = tempp >> 1
        tempq = tempq >> 1

    if test1 != 1 & test2 != 1:
        p,q = prime_gen(e)
        return p,q

    if gcd((p-1),e) != 1 & gcd((q-1),e) != 1: ##test3
        p,q = prime_gen(e)
        return p,q

    return p,q

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def privkey_gen(p,q,e): ## generate the d value, using multiplicative inverse
    bv_modulus = BitVector(intVal = ((p-1)*(q-1)))
    bv = BitVector(intVal = e)
    bv_result = bv.multiplicative_inverse( bv_modulus )
    return bv_result

def decrypt(c,d,p,q): ## decryption through Chinese Remainder Theorem and Fermat's little Theorem
    a1 = int(c)
    b1 = int(d)
    a2 = int(c)
    b2 = int(d)
    V_p = 1
    V_q = 1
    while(b1 > 0): ##Fermat's little theorem
        if(b1 & 1):
            V_p = (V_p * a1) % p
        b1 = b1 >> 1
        a1 = (a1 * a1) % p

    while(b2 > 0):
        if(b2 & 1):
            V_q = (V_q * a2) % q
        b2 = b2 >> 1
        a2 = (a2 * a2) % q

    bp = BitVector(intVal = p, size = 256) ## d = e^-1 mod p or q
    bq = BitVector(intVal = q, size = 256)
    bp_modulus = BitVector(intVal = p, size = 256)
    bq_modulus = BitVector(intVal = q, size = 256)
    bp_result = bq.multiplicative_inverse( bp_modulus )
    bq_result = bp.multiplicative_inverse( bq_modulus )
    bp_result = int(bp_result) 
    bq_result = int(bq_result)
    X_p = q*bp_result
    X_q = p*bq_result
    value = ((V_p*X_p)+(V_q*X_q)) % (p*q)
    return value

def encrypt(m,e,n):
    m=int(m)
    value = 1
    while(e > 0): ## M^e mod n
        if(e & 1):
            value = (value * m) % n
        e = e >> 1
        m = (m * m) % n
    return value

def text_fluffer(m): ##fluffs the text with 0 at the from and \n at the end
    n = BitVector(textstring = "\n")
    while len(m)<128:
        m = m + n
    m.pad_from_left(128)
    return m

def text_deflate(c):
	##removes fluff from output by taking off the leading 0's
    [left,right] = c.divide_into_two()
    return right

e=65537
if len(sys.argv) != 4:  
    sys.stderr.write("Usage: %s   -e/-d <input>.txt <output>.txt\n" % sys.argv[0]) 
    sys.exit(1)

if sys.argv[1] == "-e": ##do encrypting stuff
    inp = BitVector(filename = sys.argv[2])
    out = open(sys.argv[3],"w")
    p,q = prime_gen(e)
    key = open("key_log.txt","w")
    key.write(str(p)+"\n")
    key.write(str(q)+"\n")
    key.close()
    n=p*q
    m = inp.read_bits_from_file(128)
    
    while m:
        ot = text_fluffer(m)
        ot = encrypt(ot,e,n)
        ot = BitVector(intVal = ot, size = 64)
        ot = ot.get_hex_string_from_bitvector()
        out.write(ot)
        m = inp.read_bits_from_file(128)
    inp.close_file_object()

elif sys.argv[1] == "-d": ##do decrypting stuff
    inp =  BitVector(filename = sys.argv[2])
    out = open(sys.argv[3],"w")
    ky = open("key_log.txt","r")
    p = ky.readline()
    q = ky.readline()
    ky.close()
    p = int(p)
    q = int(q)
    d = privkey_gen(p,q,e)
    c = inp.read_bits_from_file(128)
    while c:
       c = BitVector(hexstring = c)
       ot = decrypt(c,d,p,q)
       ot = BitVector(intVal = ot, size = 128)
       ot = text_deflate(ot)
       ot = ot.get_text_from_bitvector()
       out.write(str(ot))
       c = inp.read_bits_from_file(128)
    inp.close_file_object()

out.close()