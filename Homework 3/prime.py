#!/usr/bin/env python

##Homework Number: 3
##Name: Adam Bahrainwala
##ECN Login: abahrain
##Due Date: 06/02/2014

import sys

if len(sys.argv) != 2:  
    sys.stderr.write("Usage: %s   <integer>\n" % sys.argv[0]) 
    sys.exit(1)

a = int(sys.argv[1])

def MI(num, mod):
   '''
   The function returns the multiplicative inverse (MI) of num modulo mod
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
       return 0
   else:
       MI = (x_old + MOD) % MOD
       return MI

f = open('prime.txt','w')
f.writelines("List of prime numbers in set Z_"+sys.argv[1]+"\n")
for i in range(1,a-1):
	x = MI(i,a)
	if x != 0:
		s= str(i)
		f.write(s+" is prime\n") 
	else:
		s=str(i)
		f.write(s+" is not prime\n")

f.close()
