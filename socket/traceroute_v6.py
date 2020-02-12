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
from UdpReceivingSocket4 import UdpReceivingSocket4

ADDRESS_FAMILY = socket.AF_INET6 # for IPv6
PROTOCOL_NUMBER_ICMP = socket.getprotobyname("ipv6-icmp") # for IPv4

def traceroute(dest):
    MAX_TTL = 30
    #IPv6はgetaddrinfoでIPアドレスを取得する
    #dest_addr = socket.getaddrinfo(dest_name, None)

    socket.setdefaulttimeout(15)

    ttl = 1

    while True:
        irs4 = IcmpReceivingSocket4()
        urs4 = UdpReceivingSocket4()
        uss4 = UdpSendingSocket4(dest, ttl)
        uss4.send()

        try:
            readable_sockets, writable_sockets, error_sockets = select.select([irs4.socket, urs4.socket],[],[], 15)
            if len(readable_sockets) == 0:
                raise "no readable socket"

            if readable_sockets[0] == irs4.socket:
                irs4.receive()
                print("RTT = ", (irs4.receivedTime - uss4.sentTime) * 1000, " ms", flush=True, file=sys.stderr)

            if readable_sockets[0] == urs4.socket:
                urs4.receive()
                print("RTT = ", (urs4.receivedTime - uss4.sentTime) * 1000, " ms", flush=True, file=sys.stderr)


        except socket.error:
            print (" timeout", flush=True, file=sys.stderr)

        finally:
            uss4.close()
            irs4.close()
            urs4.close()

        ttl += 1

        if irs4.receivedAddress[0] == dest or ttl > MAX_TTL:
            print("reached final destination.", flush=True, file=sys.stderr)
            break

if __name__ == "__main__":
    traceroute(str(sys.argv[1]))
