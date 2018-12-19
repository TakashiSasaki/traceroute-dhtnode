#!/usr/bin/python3 
# Bibliography
# https://qiita.com/gandarla/items/df2c5ac3f9f9485e494a
# http://d.hatena.ne.jp/addition/20130501/1367403754
# https://gist.github.com/jcjones/0f3f11a785a833e0a216

import sys
import socket
import time

ADDRESS_FAMILY = socket.AF_INET6 # for IPv6
ADDRESS_FAMILY = socket.AF_INET # for IPv4
PROTOCOL_NUMBER_ICMP = socket.getprotobyname("ipv6-icmp") # for IPv4


class UdpSocket:
    PROTOCOL_NUMBER_UDP = socket.getprotobyname("udp") 
    def __init__(self, dest, ttl):
        self.port = 33434
        self.dest = dest
        self.ttl = ttl
        self.socket = socket.socket(ADDRESS_FAMILY, socket.SOCK_DGRAM, UdpSocket.PROTOCOL_NUMBER_UDP)
        self.socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        self.buffer = bytes(512)

    def send(self):
        print("Sending UDP to ", self.dest, " with TTL = ", self.ttl, end="")
        self.socket.sendto(self.buffer, (self.dest, self.port))
        self.sentTime = time.time()
        print(" done")

    def close(self):
        self.socket.close()

class IcmpSocket:
    PROTOCOL_NUMBER_ICMP = socket.getprotobyname("icmp") # for IPv4
    def __init__(self):
        self.socket = socket.socket(ADDRESS_FAMILY, socket.SOCK_RAW, IcmpSocket.PROTOCOL_NUMBER_ICMP)

    def receive(self):
        print("Receiving ICMP .. ", end="", flush=True)
        self.receivedBytes, self.receivedAddress = self.socket.recvfrom(512)
        self.receivedTime = time.time()
        self.type = int(self.receivedBytes[20])
        self.code = int(self.receivedBytes[21])
        self.data = self.receivedBytes[24:]
        print(len(self.receivedBytes),"bytes received from ", self.receivedAddress[0], 
                ", ICMP type = ", self.type, ", ICMP code = ", self.code)
        print("ICMP payload = ", bytes.hex(self.data))
        if self.type == 3 and self.code == 1:
            print("ICMP : Host unreachable")
        elif self.type == 3 and self.code == 3:
            print("ICMP : Port unreachable")
        elif self.type == 11 and self.code == 0:
            print("ICMP : TTL equals 0 during transit")
        else:
            print("ICMP : other reason")

    def close(self):
        self.socket.close()

def traceroute(dest):
    max_hops = 30
    #IPv6はgetaddrinfoでIPアドレスを取得する
    #dest_addr = socket.getaddrinfo(dest_name, None)

    socket.setdefaulttimeout(15)

    ttl = 1

    while True:
        udpSocket = UdpSocket(dest, ttl)
        icmpSocket = IcmpSocket()
        #recv_socket = socket.socket(ADDRESS_FAMILY, socket.SOCK_RAW, PROTOCOL_NUMBER_ICMP)

        #recv_socket.bind(("", 33434))

        udpSocket.send()

        curr_addr = None
        curr_name = None


        try:
            print("Receiving ICMP .. ", end="", flush=True)
            icmpSocket.receive()
            #received_bytes, received_address = recv_socket.recvfrom(512)
            endTime = time.time()

            #icmp_type = int(received_bytes[20])
            #icmp_code = int(received_bytes[21])
            #icmp_data = received_bytes[24:]
            #print(len(received_bytes),"bytes received from ", received_address[0], 
            #        ", ICMP type = ", icmp_type, ", ICMP code = ", icmp_code)
            #print("ICMP payload = ", bytes.hex(icmp_data))
            print("RTT = ", (icmpSocket.receivedTime - udpSocket.sentTime) * 1000, " ms")


            try:
                print("FQDN = ", socket.gethostbyaddr(icmpSocket.receivedAddress[0]))
            except socket.error:
                pass

        except socket.error:
            print (" timeout")

        finally:
            udpSocket.close()
            icmpSocket.close()

        ttl += 1

        if icmpSocket.receivedAddress[0] == dest or ttl > max_hops:
            print("reached final destination.")
            break

if __name__ == "__main__":
    if len(sys.argv) == 4:
        traceroute(str(sys.argv[1]))
    else:
        traceroute("133.71.200.55")

