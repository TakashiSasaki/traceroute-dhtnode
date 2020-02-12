#!/usr/bin/python3
import sys, io, json, re
import datetime
from TableHeader import  TableHeaderException
from TableEntry import TableEntryException
from RoutingTable import RoutingTable, RoutingTableEncoder

class RoutingTablesEncoder(RoutingTableEncoder):
    def default(self, obj):
        if isinstance(obj, RoutingTables):
            return { "nodeId": obj.nodeId,
                    "routingTables": obj.routingTables}
        return RoutingTableEncoder.default(self, obj)

class RoutingTables():
    __slots__ = ["routingTables", "nodeId"]
    def __init__(self):
        self.routingTables= []
        self.nodeId = None

    def read(self, lines):
        assert(isinstance(lines,list))
        m = re.match("\s*getNodeId.*:[^0-9a-f]*([0-9a-f]+).*", lines[0])
        if m:
            self.nodeId = m[1]
            lines = lines[1:]
        while len(lines) > 0:
            routingTable = RoutingTable()
            try:
                assert(isinstance(lines, list))
                lines = routingTable.read(lines)
                assert(isinstance(lines, list))
                self.routingTables.append(routingTable)
            except TableHeaderException as e:
                return lines
            except TableEntryException as e:
                return lines

if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    routingTables = RoutingTables()
    lines = routingTables.read(lines)
    print(json.dumps(routingTables, cls=RoutingTablesEncoder))

