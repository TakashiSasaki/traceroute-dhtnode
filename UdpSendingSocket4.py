import socket,sys,time
TRACEROUTE_PORT = 33434

class UdpSendingSocket4:
    PROTOCOL_NUMBER_UDP = socket.getprotobyname("udp") 
    def __init__(self, dest, ttl):
        self.dest = dest
        self.ttl = ttl
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, UdpSendingSocket4.PROTOCOL_NUMBER_UDP)
        self.socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        self.buffer = bytes(512)

    def send(self):
        print("Sending UDP to ", self.dest, " with TTL = ", self.ttl, end="", flush=True, file=sys.stderr)
        self.socket.sendto(self.buffer, (self.dest, TRACEROUTE_PORT))
        self.sentTime = time.time()
        print(" done", flush=True, file=sys.stderr)

    def close(self):
        self.socket.close()

