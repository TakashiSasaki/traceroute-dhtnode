import opendht
import time
import datetime

class Dht():
    __slots__ = ["node", "subdir"]

    def __init__(self, subdir, bootstrapHost="bootstrap.ring.cx", bootstrapPort="4222"):
        self.subdir = subdir 
        self.node = opendht.DhtRunner()
        print(type(self.node))
        self.node.run()
        self.node.bootstrap(bootstrapHost, bootstrapPort)

    def save4(self):
        #now = datetime.datetime.now()
        fileName = self.subdir + "/" + str(int(time.time())) + ".dht4"
        f = open(fileName, "w")
        f.write("getNodeId : " + self.node.getNodeId().decode())
        f.write("\n")
        dht4 = self.node.getRoutingTablesLog(2)
        f.writelines(dht4)
        f.close()
        return fileName

    def save6(self):
        #now = datetime.datetime.now()
        fileName = self.subdir + "/" +  str(int(time.time())) + ".dht6"
        f = open(fileName, "w")
        f.write("getNodeId : " + self.node.getNodeId().decode())
        f.write("\n")
        dht6 = self.node.getRoutingTablesLog(10)
        f.writelines(dht6)
        f.close()
        return fileName

def main(subdir, interval, count):
    dht = Dht(subdir)
    time.sleep(10)
    dht.save4()
    dht.save6()
    print("DHT for IPv4 has beed saved in " + dht.save4())
    print("DHT for IPv6 has been saved in " + dht.save6())
    count -= 1
    while count != 0:
        print("waiting for {0:d} seconds".format((interval)))
        time.sleep(interval)
        print("DHT for IPv4 has beed saved in " + dht.save4())
        print("DHT for IPv6 has been saved in " + dht.save6())
        count -= 1

if __name__ == "__main__":
    import argparse, json, sys
    parser = argparse.ArgumentParser(description="Save routing tables of DHT node into files periodically.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("-c", "--count", default=1, metavar="COUNT", type=int, help='Number of times to save routing tables. Non-positive number for unlimited times.')
    parser.add_argument("-i", "--interval", default=3600, metavar="SEC", type=int, help='Time interval afthe the first log in seconds')
    parser.add_argument("-s", "--subdir",  default='dht', metavar="DIR", type=str, help='Name of the subdirectory')
    args = parser.parse_args()
    if args.dry_run is True:
        print(args)
        sys.exit()
    main(args.subdir, args.interval, args.count)
