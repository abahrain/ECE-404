#!/usr/local/bin/python

# A python implementation of a Vigene're Square.
# Please see http://gurno.com/adam/vigen/

import sys, string, rotnn

def envigen(the_key, a_string):
	ret_str = ""
	key_len = len(the_key)
	vigen_list = []
	for spot in range (0, len(a_string)):
		vigen_list.append ((a_string[spot],(ord(the_key[(spot % key_len)])-65)))
	for (let, rot_value) in vigen_list:
		ret_str = ret_str + rotnn.rotate(let, rot_value)
	return ret_str
	
def devigen(the_key, a_string):
	ret_str = ""
	key_len = len(the_key)
	vigen_list = []
	for spot in range (0, len(a_string)):
		out_char = a_string[spot]
		if (out_char in string.letters):
			key_ord = ord(the_key[(spot % key_len)])
			ciph_ord = ord(out_char)
			res_num = key_ord - ciph_ord
			if (res_num > 0):
				out_char = chr(91-res_num)
			else:
				out_char = chr(65- res_num)
		ret_str = ret_str + out_char
	return ret_str

if __name__ == '__main__':
	if (len(sys.argv) != 3):
		print 'Usage: %s "key" "phrase2encrypt"' % sys.argv[0]
		sys.exit(1)

	str_in = string.upper(string.join (string.split(sys.argv[2]), ""))
	key_str = string.upper(string.join (string.split(sys.argv[1]), ""))

	cipher_str = envigen(key_str, str_in)

	print "Ciphered:\t%s" % cipher_str

	decrypted_str = devigen(key_str, cipher_str)

	print "Unciphered:\t%s" % decrypted_str

