#!/usr/bin/python3
import re, json
sampleTableEntry1 = "Node 78e9db7ce7ec96efd9dbff32fe1d121040063fa1 185.209.190.186:5906 updated: 303 s ago, replied: never [expired]"
sampleTableEntry2 = "Node 78831ce2e065e249e8d82a95d62be8a4b651573d 51.254.39.157:4240 updated: 285 s ago [good]"
sampleTableEntry3 = "Node 7c24ea4712daa2d1133490d33b18eaf180c0a1e0 58.176.208.142:5662 updated: 6.47 s ago, replied: 1.06e+03 s ago [good]"
sampleTableEntry4 = "Node 7e207169823cfb810e334815d6c30e3054975b96 78.200.117.39:8566 updated: 827 s ago"
sampleTableEntry5 = "Node 158ee07d251e1fbc1dd95a8cb0f88d771d838e5a 192.252.140.235:4235 updated: never"

class TableEntry():
    __slots__ = ["tableEntry", "remains"]

    def __init__(self, line):
        self.tableEntry = dict()
        self.remains = None
        self.match4(line)
        if self.remains:
            self.matchRemains()
            return
        self.match6(line)
        if self.remains:
            self.matchRemains()
            return

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
    tableEntry1 = TableEntry(sampleTableEntry1)
    print(json.dumps(tableEntry1, indent=2, cls=TableEntryEncoder))
    print(tableEntry1)
    tableEntry2 = TableEntry(sampleTableEntry2)
    print(tableEntry2)
    tableEntry3 = TableEntry(sampleTableEntry3)
    print(tableEntry3)
    tableEntry4 = TableEntry(sampleTableEntry4)
    print(tableEntry4)
