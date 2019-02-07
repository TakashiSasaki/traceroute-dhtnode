#!/usr/bin/python3
import opendht as dht
import time
import datetime

node = dht.DhtRunner()
node.run()

Range = 10
Sleep = 60

node.bootstrap("bootstrap.ring.cx", "4222")

for i in range(Range):
    list = node.getRoutingTablesLog(10)
    now = datetime.datetime.now()
    fileName = "{0:%Y%m%d_%H%M%S}".format(now) + ".dhtnode-routing-table-v6"

    with open(fileName, "w") as f:
       f.writelines(list + "\n")

    time.sleep(Sleep)
