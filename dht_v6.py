import opendht as dht
import time
import datetime

node = dht.DhtRunner()
node.run()

Range = 150
Sleep = 600

node.bootstrap("bootstrap.ring.cx", "4222")

for i in range(Range):
    list = node.getRoutingTablesLog(10)
    now = datetime.datetime.now()
    filename = "/home/terao/opendht-data/v6/{0:%Y%m%d_%H%M%S}".format(now) + "v6.txt"

    with open(filename, "w") as f:
        f.writelines(list + "\n")

        time.sleep(Sleep)
