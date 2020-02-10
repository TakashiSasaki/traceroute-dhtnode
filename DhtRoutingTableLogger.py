import opendht
import time
import datetime

class Dht():
    __slots__ = ["node"]

    def __init__(self, bootstrapHost="bootstrap.ring.cx", bootstrapPort="4222"):
        self.node = opendht.DhtRunner()
        print(type(self.node))
        self.node.run()
        self.node.bootstrap(bootstrapHost, bootstrapPort)

    def save4(self):
        #now = datetime.datetime.now()
        dht4 = self.node.getRoutingTablesLog(2)
        fileName = str(int(time.time())) + ".dht4"
        with open(fileName, "w") as f:
          f.writelines(dht4)

    def save6(self):
        #now = datetime.datetime.now()
        dht6 = self.node.getRoutingTablesLog(10)
        fileName = str(int(time.time())) + ".dht6"
        with open(fileName, "w") as f:
          f.writelines(dht6)

if __name__ == "__main__":
    dht = Dht()
    time.sleep(10)
    dht.save4()
    dht.save6()
    while True:
        time.sleep(600)
        dht.save4()
        dht.save6()
