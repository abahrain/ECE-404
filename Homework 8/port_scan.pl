#!/usr/bin/perl -w

### port_scan.pl
### Author: Avi Kak  (kak@purdue.edu)

use strict;                                                         #(1)
use IO::Socket;                                                     #(2)

##  Usage example:
##
##          port_scan.pl  moonshine.ecn.purdue.edu   1  1024
##  or
##
##          port_scan.pl  128.46.144.123   1   1024

##  This script determines if a port is open simply by the act of trying
##  to create a socket for talking to the remote host through that port.

##  Assuming that a firewall is not blocking a port, a port is open if
##  and only if a server application is listening on it.  Otherwise the
##  port is closed.

##  Note that the speed of a port scan may depend critically on the
##  Timeout parameter in the socket constructor.  Ordinarily, a target
##  machine should immediately send back a RST packet for every closed
##  port.  But, as explained in Lecture 18, a firewall rule may prevent
##  that from happening.  Additionally, some older TCP implementations
##  may not send back anything for a closed port.  So if you do not set
##  the Timeout in the socket constructor, the socket constructor will
##  use some default value for the timeout and that may cause the port
##  scan to take what looks like an eternity.

##  Also note that if you set the Timeout to too small a value for a
##  congested network, all the ports may appear to be closed while that
##  is really not the case.  I usually set it to 0.1 seconds.

##  Note again that a port is considered to be closed if there is no
##  server application monitoring that port.  Most of the common servers
##  monitor ports that are below 1024.  So, if you are port scanning for
##  just fun (and not for profit), limiting your scans to ports below
##  1024 will provide you with quicker returns.

my $verbosity = 0;    # set it to 1 if you want to see              #(3)
                      # the result for each port separately
                      # as the scan is taking place

die "Usage: 'port_scan.pl host start_port  end_port' " .
    "\n where \n host is the symbolic hostname or the IP " .
    "address of the machine whose ports you want to scan " .
    "\n start_port is the starting port number and " .
    "\n end_port is the ending port number"
     unless @ARGV == 3;                                             #(4)
 
my $dst_host = shift;                                               #(5)
my $start_port = shift;                                             #(6)
my $end_port = shift;                                               #(7)

my @open_ports = ();                                                #(8)
my $testport;                                                       #(9)

# Autoflush the output supplied to print
$|++;                                                               #(10)

# Scan the ports in the specified range:
for ($testport=$start_port; $testport <= $end_port; $testport++) {  #(11)
    my $sock = IO::Socket::INET->new(PeerAddr => $dst_host,         #(12)
                                     PeerPort => $testport,         #(13)
                                     Timeout  => ".1",             #(14)
                                     Proto => 'tcp');               #(15)
    if ($sock) {                                                    #(16)
        push @open_ports, $testport;                                #(17)
        print "Open Port: ", $testport, "\n" if $verbosity == 1;    #(18)
        print  " $testport " if $verbosity == 0;                    #(19)
    } else {                                                        #(20)
        print "Port closed: ", $testport, "\n" if $verbosity == 1;  #(21)
        print "." if $verbosity == 0;                               #(22)
    }
}

# Now scan through the /etc/services file, if available, so that we can
# find out what services are provided by the open ports.  The goal here
# is to create a hash whose keys are the port names and the values
# the corresponding lines from the file that are "cleaned up" for
# getting rid of unwanted space:
my %service_ports;                                                  #(23)
if (-s "/etc/services" ) {                                          #(24)
    open IN, "/etc/services";                                       #(25)
    while (<IN>) {                                                  #(26)
        chomp;                                                      #(27)
        # Get rid of the comment lines in the file:
        next if $_ =~ /^\s*#/;                                      #(28)
        my @entry = split;                                          #(29)
        $service_ports{ $entry[1] } = join " ", 
                                      split /\s+/, $_  if $entry[1];#(30)
    }
    close IN;                                                       #(31)
}

# Now find out what services are provided by the open ports. CAUTION: 
# This information is useful only when you are sure that the target
# machine has used the designated ports for the various services.
# That is not always the case for intra-networkds:
open OUT, ">openports.txt"
         or die "Unable to open openports.txt: $!";                 #(32)
if (!@open_ports) {                                                 #(33)
    print "\n\nNo open ports in the range specified\n";             #(34)
} else {                                                            #(35)
    print "\n\nThe open ports:\n\n";                                #(36)
    foreach my $k (0..$#open_ports) {                               #(37)
        if (-s "/etc/services" ) {                                  #(38)
            foreach my $portname ( sort keys %service_ports ) {     #(39)
                if ($portname =~ /^$open_ports[$k]\//) {            #(40)
                    print "$open_ports[$k]:    $service_ports{$portname}\n";
                }                                                   #(41)
            }
        } else {                                                    #(42)
            print $open_ports[$k], "\n";                            #(43)
        }
        print OUT $open_ports[$k], "\n";                            #(44)
    }
}
close OUT;                                                          #(45)
print "\n";
