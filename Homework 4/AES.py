#!/usr/bin/env python

##Homework Number: 4
##Name: Adam Bahrainwala
##ECN Login: abahrain
##Due Date: 18/02/2014

import sys
from BitVector import *

def SubBytes(arr,box):
  ## substitute each byte from the S-Box
  for n in range(0,3):
    for t in range(0,3):
      test = arr[n,t]
      arr[n,t]=box[int(test[0,7]),int(test[8,15])]
  return arr 

def ShifRow(stray,style):
  ##shift the row the correct number of times
  if style == 1: #Encrypt
    for n in range(1,3):
      for t in range(0,n-1):
        temp = stray[n,0]
        stray[n,0] = stray[n,1]
        stray[n,1] = stray[n,2]
        stray[n,2] = stray[n,3]
        stray[n,3] = temp
  elif style == 2: #Decrypt
    for n in range(1,3):
      for t in range(0,n-1):
        temp = stray[n,3]
        stray[n,3] = stray[n,2]
        stray[n,2] = stray[n,1]
        stray[n,1] = stray[n,0]
        stray[n,0] = temp

  return stray


def ColMix(stray,style):
  ##vertically shift the columns
  base=[[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
  temp=[[0 for i in range(0,3)] for j in range(0,3)]
  m=8
  modulus = BitVector(bitstring='100011011') # AES modulus
  if style == 1: #Encrypt
    for n in range(0,3):
      for t in range(0,3):
        for k in range(0,3):
          a=BitVector(base[n,k])
          b=BitVector(stray[k,t])
          temp[n,t] += a.gf_multiply_modular(b, modulus, m)
  elif style == 2: #Decrypt
    for n in range(0,3):
      for t in range(0,3):
        for k in range(0,3):
          a=BitVector(base[n,k])
          b=BitVector(stray[k,t])
          temp[n,t] += a.gf_multiply_modular(b, modulus, m)
  return temp  

def AdRoKey(ray,key):
  ##XOR the round key with state array x^y
  out=[[0 for i in range(0,3)] for j in range(0,3)]
  for n in range(0,3):
    for t in range(0,3):
      out[n,t] = ray[n,t] ^ key[n,t]
  return out

def RokeyGen(phrase,box):
  ##generate the round keys
  k = open(phrase,'r')
  r=[[0 for i in range(0,3)] for j in range(0,63)]
  for n in range(0,3):
    for t in range(0,3):
      r[t,n] = k.read(1)
  k.close()

  for n in range(4,63):
    r[0,n] = r[3,n-1]
    r[1,n] = r[0,n-1]
    r[2,n] = r[1,n-1]
    r[3,n] = r[2,n-1]
    for t in range(0,3):
      test = r[t,n]
      r[t,n] = box[int(test[0,7]),int(test[8,15])]
    for t in range(0,3):
      r[t,n]=r[t,n]^r[t,n-4]

  return r

def SetStArray():
  ##generates State Array
  a=[[0 for i in range(0,3)] for j in range(0,3)]
  for n in range(0,3):
    for t in range(0,3):
      a[t,n] = z.read(1)
  return a

def SBox():
  ##populate the S-Box
  s=[[0 for i in range(0,15)] for j in range(0,15)]
  for r in range(0,15):
    a = BitVector(r)
    for c in range(0,15):
      b = BitVector(c)
      s[r,c]=a.gf_MI(b,8)
  return s

def Print(inform):
  for g in range(0,3):
    for h in range(0,3):
      o.write(inform[h,g])

if len(sys.argv) != 5:
  sys.stderr.write("Usage: %s encrypt/decrypt inputtext.txt key outputtext.txt\n" % sys.argv[0])
  sys.exit(1)


s_box=SBox()
key=RokeyGen(sys.argv[3])
z = open(sys.argv[2],'r')
o = open(sys.argv[4],'w')

starray=SetStArray()
if sys.argv[1] == "encrypt":
  style = 1
  for j in range(1,13):
    rkey=key[range(0,3),range(j*4,((j*4)+3))]
    starray=SubBytes(starray,s_box)
    starray=ShifRow(starray,style)
    starray=ColMix(starray,style)
    starray=AdRoKey(starray,rkey)
    Print(starray)
  rkey=key[range(0,3),range(j*4,((j*4)+3))]
  SubBytes(starray,s_box)
  ShifRow(starray,style)
  AdRoKey(starray,rkey)
  Print(starray)
  
elif sys.argv[1] == "decrypt":
  style = 2
  for j in range(14,1):  
    rkey=key[range(j*4,((j*4)+3)),range(0,3)]
    starray=ShifRow(starray,style)
    starray=SubBytes(starray,s_box)
    starray=AdRoKey(starray,rkey)
    starray=ColMix(starray,style)
    Print(starray)
  rkey=key[range(j*4,((j*4)+3)),range(0,3)]
  ShifRow(starray,style)
  SubBytes(starray,s_box)
  AdRoKey(starray,rkey)
  Print(starray)

z.close()
o.close()