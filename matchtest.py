import re
filename = "2019-12-19T18:08:29,790809551+09:00.csv"

file = open(filename)
for x in file:
    regex = re.compile("([0-9.:]+)\sIP\s([0-9.]+)\s>\s([0-9.:]+)\sICMP\s([0-9.]+)\sudp\sport\s([0-9]+)\sunreachable,\slendth([0-9]+)")
    m = regex.match(x)
    if m is None: continue
    print("time\t", m.group(1))
    print("send_IP\t", m.group(2))
    print("recv_IP\t", m.group(3))
    print("ICMP\t", m.group(4))
    print("udp_port\t", m.group(5))
    print("length\t", m.group(6))
