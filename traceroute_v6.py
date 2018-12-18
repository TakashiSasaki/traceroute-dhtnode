#bibliography
# https://qiita.com/gandarla/items/df2c5ac3f9f9485e494a
# http://d.hatena.ne.jp/addition/20130501/1367403754
# https://gist.github.com/jcjones/0f3f11a785a833e0a216

import sys
import socket
import time

def traceroute(dest_name, port, max_hops):
    #IPv6はgetaddrinfoでIPアドレスを取得する
    #dest_addr = socket.getaddrinfo(dest_name, None)
    dest_addr = dest_name


    print("target ==> %s (%s)" % (dest_name, dest_addr))

    socket.setdefaulttimeout(10)

    icmp = socket.getprotobyname('ipv6-icmp')

    udp = socket.getprotobyname('udp')

    ttl = 1

    totalRTT = 0

    while True:

        recv_socket = socket.socket(socket.AF_INET6, socket.SOCK_RAW, icmp)

        send_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, udp)

        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        recv_socket.bind(("", port))

        send_socket.sendto(bytes(512), (dest_addr, port))

        startTime = time.time()

        curr_addr = None
        curr_name = None


        try:
            curr_name, curr_addr = recv_socket.recvfrom(512)

            endTime = time.time()

            curr_addr = curr_addr[0]

            try:
                curr_name = socket.gethostbyaddr(curr_addr)[0]

            except socket.error:
                curr_name = curr_addr

        except socket.error:
            pass

        finally:
            send_socket.close()
            recv_socket.close()

            RTT = (endTime - startTime) * 1000
            totalRTT += RTT



        if curr_addr is not None:
            curr_host = "%s (%s)" % (curr_name, curr_addr)

        else:
            curr_host = "*"


        print("%d  %s" % (ttl, curr_host))
        print("   %f" % RTT + " ms")

        ttl += 1

        if curr_name == dest_name or curr_addr == dest_addr or ttl > max_hops:
            break

if __name__ == "__main__":
    traceroute(str(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

