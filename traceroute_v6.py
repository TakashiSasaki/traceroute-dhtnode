#!/usr/bin/python3 
# Bibliography
# https://qiita.com/gandarla/items/df2c5ac3f9f9485e494a
# http://d.hatena.ne.jp/addition/20130501/1367403754
# https://gist.github.com/jcjones/0f3f11a785a833e0a216

import sys
import socket
import select
import time
from UdpSendingSocket4 import UdpSendingSocket4
from IcmpReceivingSocket4 import IcmpReceivingSocket4

ADDRESS_FAMILY = socket.AF_INET6 # for IPv6
PROTOCOL_NUMBER_ICMP = socket.getprotobyname("ipv6-icmp") # for IPv4

def traceroute(dest):
    MAX_TTL = 30
    #IPv6はgetaddrinfoでIPアドレスを取得する
    #dest_addr = socket.getaddrinfo(dest_name, None)

    socket.setdefaulttimeout(15)

    ttl = 1

    while True:
        icmpSocket = IcmpReceivingSocket4()
        udpSocket = UdpSendingSocket4(dest, ttl)
        udpSocket.send()

        try:
            readable_sockets, writable_sockets, error_sockets = select.select([icmpSocket.socket],[],[],15)
            if len(readable_sockets) == 0:
                raise "no readable socket"

            if readable_sockets[0] == icmpSocket.socket:
                icmpSocket.receive()

            print("RTT = ", (icmpSocket.receivedTime - udpSocket.sentTime) * 1000, " ms", flush=True, file=sys.stderr)

        except socket.error:
            print (" timeout", flush=True, file=sys.stderr)

        finally:
            udpSocket.close()
            icmpSocket.close()

        ttl += 1

        if icmpSocket.receivedAddress[0] == dest or ttl > MAX_TTL:
            print("reached final destination.", flush=True, file=sys.stderr)
            break

if __name__ == "__main__":
    traceroute(str(sys.argv[1]))
