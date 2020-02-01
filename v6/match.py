import re
filename = "20200106_164622v6.txt"

file = open(filename)
for x in file:
    regex = re.compile("\s+Node\s+([0-9a-f]+)\s+\[([0-9a-f:]+)\]:([0-9]+)\s+.+")
    m = regex.match(x)
    if m is None: continue
    print("Node ID\t", m.group(1))
    print("Addr\t", m.group(2))
    print("Port\t", m.group(3))
