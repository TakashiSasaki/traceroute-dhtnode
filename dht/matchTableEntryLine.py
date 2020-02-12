#!/usr/bin/python3
import re
sampleTableEntry1 = "Node 78e9db7ce7ec96efd9dbff32fe1d121040063fa1 185.209.190.186:5906 updated: 303 s ago, replied: never [expired]"
sampleTableEntry2 = "Node 78831ce2e065e249e8d82a95d62be8a4b651573d 51.254.39.157:4240 updated: 285 s ago [good]"
sampleTableEntry3 = "Node 7c24ea4712daa2d1133490d33b18eaf180c0a1e0 58.176.208.142:5662 updated: 6.47 s ago, replied: 1.06e+03 s ago [good]"
sampleTableEntry4 = "Node 7e207169823cfb810e334815d6c30e3054975b96 78.200.117.39:8566 updated: 827 s ago"

def matchTableEntry(line):
    m = re.match("^\s*Node\s([0-9a-f]+)\s([0-9.]+):([0-9]+)\supdated:\s([0-9.]+)\ss\sago(.*)$", line)
    if m is None:
        return None
    tableEntry = {}
    tableEntry["node"] = m[1]
    tableEntry["ipv4"] = m[2]
    tableEntry["port"] = int(m[3])
    tableEntry["updatedAgo"] = float(m[4])
    remains = m[5]
    m2 = re.match(".*replied:\s([0-9.e+]+)\ss\sago.*", m[5])
    if m2 is None:
        tableEntry["repliedAgo"] = None
    else:
        tableEntry["repliedAgo"] = float(m2[1])
    m3 = re.match(".*\[expired\].*", m[5])
    if m3 is None:
        tableEntry["expired"] = None
    else:
        tableEntry["expired"] = True
    m4 = re.match(".*\[good\].*", m[5])
    if m4 is None:
        tableEntry["good"] = None
    else:
        tableEntry["expired"] = True
    return tableEntry

if __name__ == "__main__":
    tableEntry1 = matchTableEntry(sampleTableEntry1)
    print(tableEntry1)
    tableEntry2 = matchTableEntry(sampleTableEntry2)
    print(tableEntry2)
    tableEntry3 = matchTableEntry(sampleTableEntry3)
    print(tableEntry3)
    tableEntry4 = matchTableEntry(sampleTableEntry4)
    print(tableEntry4)
