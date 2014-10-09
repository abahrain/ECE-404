#Homework Number: 1
#Name: Adam Bahrainwala
#ECN Login: abahrain
#Due Date: 23/1/2014
import sys
import re
from BitVector import *

BLOCKSIZE = 16
numbytes = BLOCKSIZE/8
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

def product(*args, **kwds): #function taken from itertools
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def keygen(): # generates a key to try
	for length in range(16, 17): # only do lengths of 16
		to_attempt = product(chars, repeat=length) #generates the set of keys
		for attempt in to_attempt: #iterates through the set of keys
			plain = decrypt(attempt,cipher)
			if re.match(r"(.*)Mark Twain(.*)",plain): #tests decoded message for correctness
				print "Key: ",attempt
				print "Message: ",plain
				break

def decrypt(key,cipher): #Uses key to decode message
	# Reduce the key to a bit array of size BLOCKSIZE:
	key_bv = BitVector(bitlist = [0]*BLOCKSIZE)
	for i in range(0,BLOCKSIZE / numbytes):
		keyblock = key[i*numbytes:(i+1)*numbytes]
		key_bv ^= BitVector( textstring = keyblock )

	# Create a bitvector for storing the output plaintext bit array:
	msg_decrypted_bv = BitVector( size = 0 )

	# Carry out differential XORing of bit blocks and decryption:
	previous_decrypted_block = bv_iv 
	for i in range(0, len(encrypted_bv) / BLOCKSIZE):
	    bv = encrypted_bv[i*BLOCKSIZE:(i+1)*BLOCKSIZE]
 	    temp = bv.deep_copy()
	    bv ^=  previous_decrypted_block
	    previous_decrypted_block = temp
	    bv ^=  key_bv
	    msg_decrypted_bv += bv

	plain = msg_decrypted_bv.getTextFromBitVector()
	return plain

cipher = raw_input("Enter message: ")

keygen()
