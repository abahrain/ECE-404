"""
Homework Number: 2
Name: Adam Bahrainwala
ECN Login:abahrain
Due Date: 30/1/2014
"""
import sys
import BitVector


expansion_permutation = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]
round_shift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# function to handle encryption and decryption.
def crypt(round_key,way,rnd,fle):
    round_key = extract_round_key(round_key,way,rnd)
    bv = BitVector( fle )
    while (bv.more_to_read):
        bitvec = bv.read_bits_from_file( 64 )
        if bitvec.getsize() > 0:
            [LE, RE] = bitvec.divide_into_two()
            newRE = RE.permute( expansion_permutation )
            out_xor = newRE.bv_xor( round_key )
            return (out_xor,2)
# gets key from user and checks that it is 8 characters in length
def get_encryption_key():
    key=raw_input("Enter key:")
    if len(key) !=8:
        print("Invalid key")
        get_encryption_key()
    return key

# get the round key by dividing the key into two equal halves and bit shifting them
def extract_round_key(key,mode,rnd):
    bitkey=tobits(key)
    [LK, RK] = bitkey.divide_into_two()
    if mode == "encrypt":
        LK<<round_shift[rnd]
        RK<<round_shift[rnd]
    elif mode == "decrypt":
        LK>>round_shift[rnd]
        RK>>round_shift[rnd]
    return LK+RK
# converts the string to bits
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

# main
fle=raw_input("Enter file name: ")
round_key = get_encryption_key()
mode=raw_input("Enter mode <encrypt or decrypt>: ")
if mode == "encrypt" or mode == "decrypt":
    for i in range(0,16):
        out=crypt(round_key,mode,i,fle)
        print out
else:
    print("Invalid input. <encrypt or decrypt>")


"""Output:
4WQidzoTgSG4AH/Ma7hkXXYgmHjKgAI372R0RJ6yt6Wab62a2M2X/Lz3uA+rxrW3NLlE4n/fwXmtVm6Se8wwedhQHgWV4jOWkBLJZt9ko9FED5LgcXckezHYSsuzIfZAj4NoodUvIgFsajq1SoxVnHlfg1dR+kGyLDHnpwDE41lZJu0pn/gUaO5fMfCo50T954Lb0mRMYuR1xN4ixEqqZp/ZqZ5GzU5sarO2y2gT1JHft5Sd6e7c3M3huj+1aImkHAhbDQ7wdNE8WLAhEUP7ZinPe+zidxda8tsNTSnL21XiqmbDrLc4/TxPotTPDF0MXAxcr1bmDCOirYWP1SVcBkC8DOPB++L7BLyDVuXM4cRBNFp9KxLEkd38ej3UmDPqshEd4SxcGEE5wfiupMhXYhdmJoa7Q/5wEUBAu4gLHnySUhAz1TVxS0Ze4Wb+3pafACcn1w8HwqVO+mKanox142vzrHLlo2j9QX5mEtqQTiK2k21zIOX1qXi80IkBAYtrGNHug8BThxSamYNWUSUq0qNIqd6+QG65/8JFOg6mGkvJE+LAzTjRe7YXA4BCa+zHaxrMtduw0n6PuL6+rDh7HjcjJx8bHUtagjIoOYvfxndJ2d2RUZiBL2AX62WP1Ng5SVGMXqZjTqt0VEtAFKHuN9WAb4EOmLb2Hzp3hLinIyquXqnHuaJ2TvSpJAePpNwTjwW0OhSfugbQjV9P8xScduCIk8uuO7qIs+f3GpGf3SJ9XJJDcTE7+EUTNsbIvidRhTTa8W+CS87LJF8kD/8VBJWNHmL5T1q3xvJ1j2gMdgGNtzsLZh2j14XEMB82/2LpcK19Q1ejAhFOWcS4eZSFAt4OMZZwbX0Hv2s3IIqU52XaMx8wqcoYddkhStM+T4IwhplizOXK8hmwsJYEYdjIsk5NZ15ygMmlnCeAmym5rw24IUKM7InROnaNlNgPATfu2NycyeEo/H0RM42wQopkztEPYF0KdVgRBV6r2oLuhqnSw2Pgaad9Jv7S4F0uhEnOS/mWOV90tlRvnDmc9ocNt6sjwnuLOLlH59CD4yFSe9EaYDOIlE7Tcy0UXjQ63X7dirDVcQLLbua5RxYbud2UfNbQ/1le0EwHR2GXel4HOWRPpk07RxoXNFGBGv0HC6zzrffkV/6mWMYKCMxc5t1xd097/CWJyg3h+Ys4w5pic+rjnLKFWcFVkjQEy4cYyau/e5eC3Zbaz0glJ2GNfk3cTg=="""