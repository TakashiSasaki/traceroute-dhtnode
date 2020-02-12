#!/usr/bin/python3 
import sys, json
from TableHeader import  TableHeader, TableHeaderEncoder, TableHeaderException
from TableEntry import TableEntry, TableEntryEncoder, TableEntryException

class RoutingTable():
    __slots__ = ["tableHeader", "tableEntries"]
    def __init__(self):
        self.tableHeader = TableHeader()
        self.tableEntries = []

    def read(self, lines):
        lines = self.tableHeader.read(lines)
        while len(lines) > 0:
            try:
                tableEntry = TableEntry()
                lines = tableEntry.read(lines)
                self.tableEntries.append(tableEntry)
                continue
            except TableEntryException as e:
                print(e)
                return lines

class RoutingTableEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, RoutingTable):
            return {
                "tableHeader": obj.tableHeader,
                "tableEntries": obj.tableEntries
                }
        if isinstance(obj, TableHeader):
            return TableHeaderEncoder.default(self, obj)
        if isinstance(obj, TableEntry):
            return TableEntryEncoder.default(self, obj)
        return json.JSONEncoder.default(self, obj)

sampleLines1 = """0000000000000000000000000000000000000000 count: 8 updated: 584 s ago (cached)
    Node 1410ff1c8ee412728fb297f967ba8cfa43ddfe7c 51.91.75.152:58432 updated: 14 s ago, replied: 584 s ago [good]
    Node 158ee07d251e1fbc1dd95a8cb0f88d771d838e5a 192.252.140.235:4235 updated: never
    Node 0b11f6d77542b91186695814f86dd2cdda7d3d47 51.91.75.152:36126 updated: never
    Node 09df59477d0a739a271e617cf1346004707c1c38 158.69.203.11:4248 updated: never
    Node 0c16100cb988b77aa86787200e1fbf25813729ba 96.48.243.201:5022 updated: never
    Node 02e2037cc1adfe94d34749476ceacd75e9c7494b 192.252.140.235:4249 updated: never
    Node 0441cacda5ddbc7f8d1ca8e4f083e3bccb9853af 192.252.140.236:4225 updated: never
    Node 2220e7cabf0a80b7c802e1185da8b3860a2745ab 192.252.140.236:4222 updated: 584 s ago [good]"""
sampleLines2 = """4000000000000000000000000000000000000000 count: 8 updated: 307 s ago
    Node 4847a6816ffeb3abcb73deed17ee8039aaeb6b33 54.36.178.20:4238 updated: 307 s ago [good]
    Node 457901da1ed0f25560f95f5f18593fb833fc5506 54.36.178.20:4246 updated: 566 s ago [good]
    Node 43b53ba67090b1b81f61e31a3cddcf3403ed7ffb 67.253.17.207:5270 updated: 10.7 s ago, replied: 566 s ago [good]
    Node 40160730144edf99de5a9852db8ac93016280472 51.91.75.152:34913 updated: never
    Node 4090a86b1413702c07d841f1b672b6e8106f2898 158.69.203.51:4243 updated: never
    Node 50a37e58c63a25a9310fdee40328b1940ba1c970 192.252.140.236:4235 updated: 1.17e+03 s ago
    Node 50c94e29e4cd7549992d34eb253ec02612f4a0df 51.77.188.15:5702 updated: 566 s ago [good]
    Node 5e90112da31bb863d4ac141ac23e1afc28757c6d 192.252.140.236:4240 updated: 1.21e+03 s ago
"""

if __name__ == "__main__":
    #lines = open(sys.argv[1], "r").readlines()
    routingTable1 = RoutingTable()
    routingTable1.read(sampleLines1.split("\n"))
    print(json.dumps(routingTable1, cls=RoutingTableEncoder))
    routingTable2 = RoutingTable()
    routingTable2.read(sampleLines2.split("\n"))
    print(json.dumps(routingTable2, cls=RoutingTableEncoder))
