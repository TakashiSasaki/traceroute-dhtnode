import sys
import socket
import time

def traceroute(dest_name):

    global endTime
    dest_addr = dest_name
    port = 33434   
    max_hops = 50


    sys.stderr.write("target ==> %s (%s) \n" % (dest_name, dest_addr))

    #timeout
    socket.setdefaulttimeout(10)

    icmp = socket.getprotobyname('icmp')

    ttl = 1

    totalRTT = 0 

    while True:

        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, icmp)

        send_socket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)

        send_socket.bind(("", port))

        send_socket.sendto(bytes(512), (dest_addr, port))
   
        startTime = time.perf_counter()

        curr_addr = None
        curr_name = None


        try:

            curr_name, curr_addr = recv_socket.recvfrom(512)

            endTime = time.perf_counter()

            curr_addr = curr_addr[0]

        except socket.error:
            pass

        finally:
            send_socket.close()
        try:
            RTT = (endTime - startTime) * 1000
            totalRTT += RTT
        except NameError:
            pass

        if curr_addr is not None:
             curr_host = "%s" % (curr_addr)

        #timeout
        else:
            curr_host = "*"
            RTT = None


        sys.stderr.write("%d  %s" % (ttl, curr_host))

        if RTT is not None:
            sys.stderr.write("   %f" % RTT + " ms \n")

            print("%d, %s, %f" % (ttl, curr_addr, RTT))

        else:
            sys.stderr.write("   %s" % RTT + " ms \n")

            print("%d, %s, %s" % (ttl, curr_addr, RTT))


        ttl += 1

        if curr_addr == dest_addr or ttl > max_hops:
            break

if __name__ == "__main__":
    traceroute(str(sys.argv[1]))
