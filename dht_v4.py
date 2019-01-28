import opendht as dht
import time
import datetime

node = dht.DhtRunner()
node.run()

Range = 121
Sleep = 600

node.bootstrap("bootstrap.ring.cx", "4222")

for i in range(Range):
    list = node.getRoutingTablesLog(2)

    now = datetime.datetime.now()

    fileName = "/home/pi/python/exp/OpenDHT/v4/{0:%Y%m%d_%H%M%S}".format(now) + ".txt"

    with open(fileName, "w") as f:
       f.writelines(list + "\n")

    time.sleep(Sleep)
