#!/usr/bin/python3
import re, json
sampleTableEntry1 = "Node 78e9db7ce7ec96efd9dbff32fe1d121040063fa1 185.209.190.186:5906 updated: 303 s ago, replied: never [expired]"
sampleTableEntry2 = "Node 78831ce2e065e249e8d82a95d62be8a4b651573d 51.254.39.157:4240 updated: 285 s ago [good]"
sampleTableEntry3 = "Node 7c24ea4712daa2d1133490d33b18eaf180c0a1e0 58.176.208.142:5662 updated: 6.47 s ago, replied: 1.06e+03 s ago [good]"
sampleTableEntry4 = "Node 7e207169823cfb810e334815d6c30e3054975b96 78.200.117.39:8566 updated: 827 s ago"
sampleTableEntry5 = "Node 158ee07d251e1fbc1dd95a8cb0f88d771d838e5a 192.252.140.235:4235 updated: never"
sampleTableEntry6 = "Node 0b7fb4343df5d0dd526be47ae9f90c7086d04a8d [2607:fad8:4:6:dd0c:1922:7704:6a45]:8422 updated: 595 s ago, replied: 2.39e+03 s ago [good]"
sampleTableEntry7 = "Node 3c13edb6c848c78e8189fc432f210a58155856de [2001:41d0:403:3398::]:55063 updated: 424 ms ago, replied: 2.4e+03 s ago [good]"
class TableEntryException(RuntimeError):
    pass

class TableEntry():
    __slots__ = ["tableEntry", "remains"]

    def __init__(self):
        self.tableEntry = dict()
        self.remains = None

    def read(self, lines):
        self.match4(lines[0])
        if self.remains:
            self.matchRemains()
            return lines[1:]
        self.match6(lines[0])
        if self.remains:
            self.matchRemains()
            return lines[1:]
        raise TableEntryException(lines[0])

    def match4(self,line):
        m = re.match("^\s*Node\s([0-9a-f]+)\s([0-9.]+):([0-9]+)\s(.*)$", line)
        if m is None:
            return None
        self.tableEntry = {}
        self.tableEntry["node"] = m[1]
        self.tableEntry["ipv4"] = m[2]
        self.tableEntry["port"] = int(m[3])
        self.remains = m[4]

    def match6(self,line):
        m = re.match("^\s*Node\s([0-9a-f]+)\s\[([0-9a-f:]+)\]:([0-9]+)\s(.*)$", line)
        if m is None:
            return None
        self.tableEntry = {}
        self.tableEntry["node"] = m[1]
        self.tableEntry["ipv6"] = m[2]
        self.tableEntry["port"] = int(m[3])
        self.remains = m[4]

    def matchRemains(self):
        m1 = re.match(".*updated:\s([0-9.e+]+)\ss\sago.*", self.remains)
        if m1 is None:
            self.tableEntry["updatedAgo"] =  None
        else:
            self.tableEntry["updatedAgo"] = float(m1[1])
        m2 = re.match(".*replied:\s([0-9.e+]+)\ss\sago.*", self.remains)
        if m2 is None:
            self.tableEntry["repliedAgo"] = None
        else:
            self.tableEntry["repliedAgo"] = float(m2[1])
        m3 = re.match(".*\[expired\].*", self.remains)
        if m3 is None:
            self.tableEntry["expired"] = None
        else:
            self.tableEntry["expired"] = True
        m4 = re.match(".*\[good\].*", self.remains)
        if m4 is None:
            self.tableEntry["good"] = None
        else:
            self.tableEntry["expired"] = True

    def __dict__(self):
        return self.tableEntry

class TableEntryEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, TableEntry):
            return obj.tableEntry
        return json.JSONEncoder.default(self, obj)

if __name__ == "__main__":
    tableEntry1 = TableEntry()
    tableEntry1.read([sampleTableEntry1])
    print(json.dumps(tableEntry1, cls=TableEntryEncoder))
    tableEntry2 = TableEntry()
    tableEntry2.read([sampleTableEntry2])
    print(json.dumps(tableEntry2, cls=TableEntryEncoder))
    tableEntry3 = TableEntry()
    tableEntry3.read([sampleTableEntry3])
    print(json.dumps(tableEntry3, cls=TableEntryEncoder))
    tableEntry4 = TableEntry()
    tableEntry4.read([sampleTableEntry4])
    print(json.dumps(tableEntry4, cls=TableEntryEncoder))
    tableEntry5 = TableEntry()
    tableEntry5.read([sampleTableEntry5])
    print(json.dumps(tableEntry5, cls=TableEntryEncoder))
    tableEntry6 = TableEntry()
    tableEntry6.read([sampleTableEntry6])
    print(json.dumps(tableEntry6, cls=TableEntryEncoder))
    tableEntry7 = TableEntry()
    tableEntry7.read([sampleTableEntry7])
    print(json.dumps(tableEntry7, cls=TableEntryEncoder))

