from scapy.all import *

def send_icmpv6_echo_request():
    ipv6 = IPv6()
    #ipv6.dst = "fe80:0:0:0:e99f:749e:93aa:f3d9"
    ipv6.dst = "ff02::1"
    icmpv6_echo_request = ICMPv6EchoRequest()
    frame = Ether() / ipv6 / icmpv6_echo_request
    sendp(frame)


send_icmpv6_echo_request()

def send_icmpv6_ind_sol(mac):
    ether = Ether()
    ether.dst = mac
    ipv6 = IPv6()
    ipv6.dst = "ff02::1"
    icmpv6_ind_sol = ICMPv6ND_INDSol()
    frame = Ether() / ipv6 / icmpv6_ind_sol
    sendp(frame)



send_icmpv6_ind_sol("b8:27:eb:46:00:9d")
send_icmpv6_ind_sol("ff:ff:ff:ff:ff:ff")
send_icmpv6_ind_sol("c4:9d:ed:90:27:1c")
send_icmpv6_ind_sol("a8:60:b6:2b:b5:5d")
send_icmpv6_ind_sol("40:8d:5c:bf:37:d9")
send_icmpv6_ind_sol("40:8d:5c:bf:37:4a")
send_icmpv6_ind_sol("b8:27:eb:8b:88:11")
send_icmpv6_ind_sol("e4:f0:42:11:35:62")
send_icmpv6_ind_sol("1c:1b:0d:99:21:9d")
send_icmpv6_ind_sol("00:3a:9d:dd:37:a0")
send_icmpv6_ind_sol("00:08:9b:cb:5a:9d")
send_icmpv6_ind_sol("a0:0b:ba:d4:a8:7c")
send_icmpv6_ind_sol("4c:cc:6a:01:39:8c")
send_icmpv6_ind_sol("00:08:9b:cb:5a:9c")
send_icmpv6_ind_sol("40:8d:5c:be:c4:eb")
send_icmpv6_ind_sol("00:26:73:e9:d9:a5")
send_icmpv6_ind_sol("a8:60:b6:2b:b5:5d")
send_icmpv6_ind_sol("00:a0:de:c6:38:b6")
send_icmpv6_ind_sol("40:8d:5c:b8:e0:da")
send_icmpv6_ind_sol("84:b5:9c:8a:fb:41")
send_icmpv6_ind_sol("d8:cb:8a:1a:8b:35")
send_icmpv6_ind_sol("f8:0d:60:ce:f0:a5")
send_icmpv6_ind_sol("40:8d:5c:bf:79:a6")
send_icmpv6_ind_sol("00:16:3e:2a:a5:af")
send_icmpv6_ind_sol("20:cf:30:3a:69:46")
send_icmpv6_ind_sol("40:8d:5c:be:c5:1e")
send_icmpv6_ind_sol("40:8d:5c:b8:e0:90")
send_icmpv6_ind_sol("00:0c:29:ba:e9:09")
send_icmpv6_ind_sol("00:16:3e:3a:f4:92")
send_icmpv6_ind_sol("20:cf:30:3a:66:7b")
send_icmpv6_ind_sol("cc:e1:d5:a5:5a:5b")
send_icmpv6_ind_sol("b8:27:eb:27:8f:da")
send_icmpv6_ind_sol("40:8d:5c:bc:83:22")
send_icmpv6_ind_sol("40:8d:5c:b4:69:be")


