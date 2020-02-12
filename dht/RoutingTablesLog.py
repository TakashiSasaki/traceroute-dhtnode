#!/usr/bin/python3
import datetime,sys,re
from RoutingTables import RoutingTables

class RoutingTablesLog():
    __slots__ = ["awareTimestamp", "routingTables"]

    def __init__(self, filename):
        m = re.match("([0-9]+).*", filename)
        if m is None:
            raise RuntimeError("file name should begin with UNIX epoch as a part of it.")
        print(m[1])
        second = int(m[1])
        assert(second > 1500000000)
        self.awareTimestamp = datetime.datetime.fromtimestamp(second, datetime.timezone.utc)
        assert(self.awareTimestamp.tzinfo is not None)
        f = open(filename, "r")
        lines = f.readlines()
        self.routingTables = RoutingTables()
        self.routingTables.read(lines)

    def __dict__(self):
        return {"awareTimestamp": self.awareTimestamp,
                "routingTables": self.routingTables}

if __name__ == "__main__":
    routingTablesLog = RoutingTablesLog(sys.argv[1])
    print(routingTablesLog.__dict__())

