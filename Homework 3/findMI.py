#!/usr/bin/env python

### Author: Avi Kak

### This is a command-line version of IntegerMI.py

### It is meant to be called as
###
###      findMI 17 120
###
### if you want to find the multiplicative inverse of 17 modulo 120


###  This is for finding multiplicative inverses using ordinary
###  integer arithmetic.    If you need to find multiplicative
###  inverses in Galois Field GF(2^n), use the file TestMI.py
###  or the BitVector class directly.


import sys

#if len( sys.argv ) != 3:
#    sys.exit( "Call syntax:  findMI number1 number2" )

if len(sys.argv) != 3:                                                                     
    sys.stderr.write("Usage: %s   <integer>   <modulus>\n" % sys.argv[0])                  
    sys.exit(1) 

a = int( sys.argv[1] )
p = int( sys.argv[2] )

# The following uses ordinary number arithmetic to find the
# MI of one integer vis-a-vis another integer.
def MI(num, mod):
    '''
    The function returns the multiplicative inverse (MI)
    of num modulo mod
    '''
    NUM = num; MOD = mod
    x, x_old = 0L, 1L
    y, y_old = 1L, 0L
    while mod:
        q = num // mod
        num, mod = mod, num % mod
        x, x_old = x_old - q * x, x
        y, y_old = y_old - q * y, y
    if num != 1:
        return "NO MI. However, the GCD of %d and %d is %u" % (NUM, MOD, num)
    else:
        MI = (x_old + MOD) % MOD
        return MI

x = MI(a, p)
print "MI of ", a, " modulo ", p, " is: ", x


