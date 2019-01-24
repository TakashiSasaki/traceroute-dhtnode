from scapy.all import *
ipv6 = IPv6()
ipv6.dst = "fe80:0:0:0:e99f:749e:93aa:f3d9"
icmpv6_echo_request = ICMPv6EchoRequest()
frame = Ether() / ipv6 / icmpv6_echo_request
sendp(frame)

