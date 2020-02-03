import re, json

sample = """14:35:42.235983 IP (tos 0x0, ttl 46, id 50727, offset 0, flags [none], proto ICMP (1), length 145)
    162.218.44.28 > 133.71.3.62: ICMP 162.218.44.28 udp port 1027 unreachable, length 125
	IP (tos 0x0, ttl 44, id 54376, offset 0, flags [DF], proto UDP (17), length 117)
    133.71.3.62.33419 > 162.218.44.28.1027: UDP, length 89"""

class HostUnreachableMatcher():
    __slots__ = ["lines", "o"]

    def __init__(self, lines=None):
        if(lines is None):
            lines = sample.splitlines()
            #print(len(lines))
            self.lines = lines

        if len(lines) != 4:
            raise RuntimeError("The number of lines is not four.")
        self.lines = lines
        self.o = {}
        self.match1()

    def match1(self):
        l = self.lines[0]
        m = re.match("^(\d\d):(\d\d):(\d\d)\.(\d+)\sIP\s(.*)$",l)
        self.o["hour"] = m[1]
        self.o["minute"] = m[2]
        self.o["second"] = m[3]
        self.o["fraction"] = m[4]
        #print(m[5])
        m = re.match("^\(tos\s+([0-9x]+),\s+ttl\s+(\d+),\s+id\s+(\d+),\s+(.*)$", m[5])
        self.o["tos"] = m[1]
        self.o["ttl"] = m[2]
        self.o["id"] = m[3]
        m = re.match("^offset\s+(\d+),\s+flags\s+(.*)$", m[4])
        self.o["offset"] = m[1]
        m = re.match("^(\[.*\]),\s+(.*)$", m[2])
        self.o["flags"] = m[1]
        m = re.match("^proto\s+ICMP\s+\((\d+)\),\s+(.*)$", m[2])
        self.o["icmpCode"] = m[1]
        m = re.match("^length\s+(\d+)\)\s*$", m[2])
        self.o["length"] = m[1]
        #print(m)
        #print(o)

    def __getitem__(self, key):
        return 

    def __str__(self):
        return json.dumps(self.o)

if __name__ == "__main__":
    matcher = HostUnreachableMatcher()
    print(matcher)

