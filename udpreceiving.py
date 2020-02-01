import socket,sys,time
PROTOCOL_NUMBER = socket.getprotobyname("udp")

class UdpReceivingSocket4:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DREAM, PROTOCOL_NUMBER)

        def receive(self):
            print("Receiving UDP .. ",end="", flush=True, file=sys.stderr)
            self.receivedBytes, self.receivedAddress = self.socket.recvfrom(512)
            self.receivedTime = time.time()
            print(len(self.receivedBytes),"bytes received from ",self.receivedAddress[0])

            def close(self):
                self.socket.close()
