#!/usr/bin/env python

##Homework Number: 3
##Name: Adam Bahrainwala
##ECN Login: abahrain
##Due Date: 06/02/2014

import sys

if len(sys.argv) != 3:  
    sys.stderr.write("Usage: %s   <integer>   <modulus>\n" % sys.argv[0]) 
    sys.exit(1) 

def BIMI(num,mod):
    NUM = num; MOD = mod
    x, x_old = 0L, 1L
    y, y_old = 1L, 0L
    while mod:
        q = num >> mod
        num, mod = mod, num % mod
        x, x_old = x_old - q << x, x
        y, y_old = y_old - q << y, y
    if num != 1:
        return 0
    else:
        MI = (x_old + MOD) % MOD
        return MI

f = open("mi.txt","w")
x=BIMI(int(sys.argv[1]),int(sys.argv[2]))
if x != 0:
    s = str(x)
    f.write("Mulitplicative Inverse: "+ s)
else:
    f.write("No multiplicative inverse exists.")

f.close()

"""
15%4
Mulitplicative Inverse: 3
76435%4
Mulitplicative Inverse: 3
465135354%354318437468743
Mulitplicative Inverse: 202759811091371
"""



