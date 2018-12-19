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
PROTOCOL_NUMBER_ICMP = socket.getprotobyname("icmp") # for IPv4


class UdpSocket:
    PROTOCOL_NUMBER_UDP = socket.getprotobyname("udp") 
    def __init__(self, dest, port, ttl):
        self.dest = dest
        self.port = port
        self.ttl = ttl
        self.socket = socket.socket(ADDRESS_FAMILY, socket.SOCK_DGRAM, UdpSocket.PROTOCOL_NUMBER_UDP)
        self.socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        self.buffer = bytes(512)

    def send(self):
        print("Sending UDP to ", self.dest, " with TTL = ", self.ttl, end="")
        self.socket.sendto(self.buffer, (self.dest, self.port))
        self.sendTime = time.time()
        print(" done")

    def close(self):
        self.socket.close()

def traceroute(dest_name, port, max_hops):
    #IPv6はgetaddrinfoでIPアドレスを取得する
    #dest_addr = socket.getaddrinfo(dest_name, None)
    dest_addr = dest_name


    socket.setdefaulttimeout(15)

    ttl = 1

    while True:
        udpSocket = UdpSocket(dest_name, port, ttl)
        recv_socket = socket.socket(ADDRESS_FAMILY, socket.SOCK_RAW, PROTOCOL_NUMBER_ICMP)

        recv_socket.bind(("", port))

        udpSocket.send()

        curr_addr = None
        curr_name = None


        try:
            print("Receiving ICMP .. ", end="", flush=True)
            received_bytes, received_address = recv_socket.recvfrom(512)
            endTime = time.time()

            icmp_type = int(received_bytes[20])
            icmp_code = int(received_bytes[21])
            icmp_data = received_bytes[24:]
            print(len(received_bytes),"bytes received from ", received_address[0], 
                    ", ICMP type = ", icmp_type, ", ICMP code = ", icmp_code)
            print("ICMP payload = ", bytes.hex(icmp_data))
            print("RTT = ", (endTime - udpSocket.sendTime) * 1000, " ms")

            if icmp_type == 3 and icmp_code == 1:
                print("ICMP : Host unreachable")
            elif icmp_type == 3 and icmp_code == 3:
                print("ICMP : Port unreachable")
            elif icmp_type == 11 and icmp_code == 0:
                print("ICMP : TTL equals 0 during transit")
            else:
                print("ICMP : other reason")

            try:
                print("FQDN = ", socket.gethostbyaddr(received_address[0]))
            except socket.error:
                pass

        except socket.error:
            print (" timeout")

        finally:
            udpSocket.close()
            recv_socket.close()

        ttl += 1

        if curr_name == dest_name or curr_addr == dest_addr or ttl > max_hops:
            print("reached final destination.")
            break

if __name__ == "__main__":
    if len(sys.argv) == 4:
        traceroute(str(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    else:
        traceroute("133.71.200.55", 1000, 20)

