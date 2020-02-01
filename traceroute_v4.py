import sys
import socket
import time

def traceroute(dest_name):

    dest_addr = dest_name
    port = 33434
    max_hops = 50

    sys.stderr.write("target ==> %s (%s) \n" % (dest_name, dest_addr))
    
    socket.setdefaulttimeout(2)

    icmp = socket.getprotobyname('icmp')

    udp = socket.getprotobyname('udp')

    ttl = 1

    totalRTT = 0
    
    while True:

        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DREAM, udp)

        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        recv_socket.bind(("", port))

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
                recv_socket.close()

                RTT = (endTime - startTime) * 1000
                totalRTT += RTT

                if curr_addr is not None:
                    curr_host = "%s" % (curr_addr)

                else:
                    curr_host = "*"
                    RTT = None

                    sys.stderr.write("%d %s" % (ttl, curr_host))

                    if RTT is not None:
                        sys.stderr.write("  %f" % RTT + " ms \n")

                        print("%d, %s, %f" % (ttl, curr_addr, RTT))

                    else:
                        sys.stderr.write("  %s" % RTT + " ms \n")

                        print("%d, %s, %s" % (ttl, curr_addr, RTT))

                        ttl += 1

                        if curr_addr == dest_addr or ttl > max_hops:
                            break

                        if __name__ == "__main__":
                            traceroute(str(sys.argv[1]))
