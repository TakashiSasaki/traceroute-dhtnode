#!/usr/bin/python3 
# Bibliography
# https://qiita.com/gandarla/items/df2c5ac3f9f9485e494a
# http://d.hatena.ne.jp/addition/20130501/1367403754
# https://gist.github.com/jcjones/0f3f11a785a833e0a216

import sys
import socket
import time

ADDRESS_FAMILY = socket.AF_INET6 # for IPv6
PROTOCOL_NUMBER_ICMP = socket.getprotobyname("ipv6-icmp") # for IPv4


class UdpSocket:
    ADDRESS_FAMILY = socket.AF_INET # for IPv4
    PROTOCOL_NUMBER_UDP = socket.getprotobyname("udp") 
    def __init__(self, dest, ttl):
        self.port = 33434
        self.dest = dest
        self.ttl = ttl
        self.socket = socket.socket(UdpSocket.ADDRESS_FAMILY, socket.SOCK_DGRAM, UdpSocket.PROTOCOL_NUMBER_UDP)
        self.socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        self.buffer = bytes(512)

    def send(self):
        print("Sending UDP to ", self.dest, " with TTL = ", self.ttl, end="", flush=True, file=sys.stderr)
        self.socket.sendto(self.buffer, (self.dest, self.port))
        self.sentTime = time.time()
        print(" done", flush=True, file=sys.stderr)

    def close(self):
        self.socket.close()

class IcmpSocket:
    ADDRESS_FAMILY = socket.AF_INET # for IPv4
    PROTOCOL_NUMBER_ICMP = socket.getprotobyname("icmp") # for IPv4
    def __init__(self):
        self.socket = socket.socket(IcmpSocket.ADDRESS_FAMILY, socket.SOCK_RAW, IcmpSocket.PROTOCOL_NUMBER_ICMP)

    def receive(self):
        print("Receiving ICMP .. ", end="", flush=True, file=sys.stderr)
        self.receivedBytes, self.receivedAddress = self.socket.recvfrom(512)
        self.receivedTime = time.time()
        self.type = int(self.receivedBytes[20])
        self.code = int(self.receivedBytes[21])
        self.data = self.receivedBytes[24:]
        print(len(self.receivedBytes),"bytes received from ", self.receivedAddress[0], 
                ", ICMP type = ", self.type, ", ICMP code = ", self.code, flush=True, file=sys.stderr)
        print("ICMP payload = ", bytes.hex(self.data), flush=True, file=sys.stderr)
        if self.type == 3 and self.code == 1:
            print("ICMP : Host unreachable", flush=True, file=sys.stderr)
        elif self.type == 3 and self.code == 3:
            print("ICMP : Port unreachable", flush=True, file=sys.stderr)
        elif self.type == 11 and self.code == 0:
            print("ICMP : TTL equals 0 during transit", flush=True, file=sys.stderr)
        else:
            print("ICMP : other reason", flush=True, file=sys.stderr)

    def close(self):
        self.socket.close()

def traceroute(dest):
    MAX_TTL = 30
    #IPv6はgetaddrinfoでIPアドレスを取得する
    #dest_addr = socket.getaddrinfo(dest_name, None)

    socket.setdefaulttimeout(15)

    ttl = 1

    while True:
        icmpSocket = IcmpSocket()
        udpSocket = UdpSocket(dest, ttl)
        udpSocket.send()

        try:
            icmpSocket.receive()
            print("RTT = ", (icmpSocket.receivedTime - udpSocket.sentTime) * 1000, " ms", flush=True, file=sys.stderr)

            try:
                print("FQDN = ", socket.gethostbyaddr(icmpSocket.receivedAddress[0]), flush=True, file=sys.stderr)
            except socket.error:
                pass

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
