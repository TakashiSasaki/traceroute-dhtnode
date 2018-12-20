import socket,sys,time
PROTOCOL_NUMBER= socket.getprotobyname("icmp") # for IPv4

class IcmpReceivingSocket4:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, PROTOCOL_NUMBER)

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

