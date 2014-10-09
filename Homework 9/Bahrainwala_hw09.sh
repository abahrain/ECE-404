#! /bin/bash
##Homework Number: 9
##Name: Adam Bahrainwala
##ECN Login: abahrain
##Due Date: 03/04/2014
iptables -A INPUT -p tcp --src 128.210.7.199 --destination-port 22 -j ACCEPT ##Allow ssh port 22 only for purdue.edu domain
iptables -A INPUT -p tcp --destination-port 80 -j ACCEPT ##Accept connection for HTTPD
iptables -A INPUT -p tcp --dport 113 -j ACCEPT ##Accept smtp connections
iptables -A INPUT -p tcp -j REJECT ##Reject all tcp traffic
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT ##Accept ICMP echo requests
iptables -A INPUT -p icmp -j REJECT ##Reject all icmp traffic
iptables -A OUTPUT -j ACCEPT ##No restrictions on outbound traffic
