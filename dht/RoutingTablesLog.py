#!/usr/bin/python3
import datetime,sys,re
from RoutingTables import RoutingTables

class RoutingTablesLog(RoutingTables):
    __slots__ = ["awareTimestamp"]

    def __init__(self, filename):
        m = re.match(".*([0-9]+).*", filename)
        if m is None:
            raise RuntimeError("file name should contain UNIX epoch as a part of it.")
        awareTimestamp = datetime.datetime.fromtimestamp(int(m[1]), datetime.timezone.utc)
        f = open(filename, "r")
        lines = f.readlines()
        routingTables = RoutingTables(lines)

        if awareTimestamp:
            if awareTimestamp.tzinfo is None:
                raise RuntimeError("timestamp should be aware datetime.datetime object.")
        RoutingTables.__init__(self, lines)

if __name__ == "__main__":
    routingTablesLog = RoutingTablesLog(sys.argv[1])
    print(routingTablesLog.nodeId)

