import re
filename = "2019-12-19T18:08:29,790809551+09:00"
file = open(filename)
for x in file:
    regex_type1 = re.compile("([0-9:.]+)\sIP\s+([0-9.]+)\s>\s([0-9.]+):\sICMP\s([0-9.]+)\sudp\sport\s([0-9]+)\sunreachable,\slength\s([0-9]+)")
    m_type1 = regex_type1.match(x)
    regex_type2 = re.compile("([0-9:.]+)\sIP\s+([0-9.]+)\s>\s([0-9.]+):\sICMP\secho\s([a-z,]+)\sid\s1,\sseq\s([0-9,]+)\slength\s([0-9]+)")
    m_type2 = regex_type2.match(x)
    if m_type1 is not None:
        print("time\t", m_type1.group(1))
        print("send_IP\t", m_type1.group(2))
        print("recv_IP\t", m_type1.group(3))
        print("ICMP\t", m_type1.group(4))
        print("udp_port\t", m_type1.group(5))
        print("length\t", m_type1.group(6))
    elif m_type2 is not None:
        print("time\t", m_type2.group(1))
        print("send_IP\t", m_type2.group(2))
        print("recv_IP\t", m_type2.group(3))
        print("ICMP\t", m_type2.group(4))
        print("ID\t", m_type2.group(5))
        print("seq\t", m_type2.group(6))
        print("length\t", m_type2.group(7))
