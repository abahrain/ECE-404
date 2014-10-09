#Homework Number: 1
#Name: Adam Bahrainwala
#ECN Login: abahrain
#Due Date: 23/1/2014
import sys
import string

def vigen(key, text):
    cyp_str = ""
    key_len = len(key)
    gen_list = []
    for place in range (0, len(text)):
        gen_list.append ((text[place],(ord(key[(place % key_len)])-65)))
    for (let, rot_value) in gen_list:
        cyp_str = cyp_str + rotate(let, rot_value)
    return cyp_str

def rotate(a_string, amount=13):
        if (amount > 26) or (amount < 0):
                raise ValueError, "Invalid Rotation Value"
        char_list = []
        for single_char in a_string:
                ord_char = ord(single_char)
                if (65 <= ord_char <= (90-amount)) or (97 <= ord_char <= (122-amount)):
                        char_list.append (chr(ord_char + amount))
                elif ((91-amount) <= ord_char <= 90):
                        char_list.append (chr(65 + (amount - (91 - ord_char))))
                elif ((123-amount) <= ord_char <= 122):
                        char_list.append (chr(97 + (amount - (123 - ord_char))))
                else:
                        char_list.append (chr(ord_char))
        rot_str = string.join(char_list,"")
        return (rot_str)

text = raw_input("Enter message: ")
key = raw_input("Enter key: ") 
plain = string.upper(string.join (string.split(text), ""))
key = string.upper(string.join (string.split(key), ""))

cipher = vigen(key, plain)

print "Ciphered:\t%s" % cipher
