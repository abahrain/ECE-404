#!/usr/bin/env python

##Homework Number: 5
##Name: Adam Bahrainwala
##ECN Login: abahrain
##Due Date: 25/02/2014

import wave
import sys

#RC4 Implementation
def rc4_crypt( data , key ):
    
    S = range(256)
    j = 0
    out = []
    
    #KSA Phase
    for i in range(256):
        j = (j + S[i] + ord( key[i % len(key)] )) % 256
        S[i] , S[j] = S[j] , S[i]
    
    #PRGA Phase
    for char in data:
        i,j = 0
        i = ( i + 1 ) % 256
        j = ( j + S[i] ) % 256
        S[i] , S[j] = S[j] , S[i]
        out.append(S[(S[i] + S[j]) % 256])
        
    return ''.join(out)

#checks that there are enough arguments
if len(sys.argv) != 4:  
    print (" Usage: <data> <key> <output>")
    sys.exit(1)

data = wave.open(sys.argv[1],'r') #opens the input file
length = data.getnframes() #gets length of input file
out = wave.open(sys.argv[3],'w') #open output file
key  = tuple(sys.argv[2]) #set key as tuple so that it is more easily read

for i in range(0,length):
	dat = data.readframes(1) #set data to segment of input file
	da = rc4_crypt(dat, key)
	out.writeframes(da) #print to output

#close files    
data.close()
out.close()


