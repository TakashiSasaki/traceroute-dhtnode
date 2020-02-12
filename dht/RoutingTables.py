#!/usr/bin/python3
import sys, io, json, re
import datetime
from matchTableHeaderLine import matchTableHeaderLine
from matchTableEntryLine import matchTableEntryLine

class RoutingTable(json.JSONEncoder):
    __slots__ = ["tableHeader", "tableEntries"]
    def __init__(self, tableHeader):
        self.tableHeader = tableHeader
        self.tableEntries = []

    def addTableEntry(self, tableEntry):
        self.tableEntries.append(tableEntry)

def serialize(o):
    if isinstance(o, (datetime.datetime)):
        return o.isoformat()
    if isinstance(o, RoutingTable):
        serializable = dict() 
        serializable["tableHeader"] = o.tableHeader
        serializable["tableEntries"] = o.tableEntries
        return serializable
    raise TypeError ("Type %s not serializable" % type(o))

class RoutingTables():
    __slots__ = ["tables", "nodeId"]
    def __init__(self, lines):
        self.tables = []
        i = 0
        while i < len(lines):
            line = lines[i]
            m = re.match("\s*getNodeId.*:[^0-9a-f]*([0-9a-f]+).*", line)
            if m:
                self.nodeId = m[1]
                i += 1
                continue
            o = matchTableHeaderLine(line)
            if o is None:
                raise RuntimeError("expecting table header line while got : " + line)
            table = RoutingTable(o)
            i += 1
            while i < len(lines):
                line = lines[i]
                o = matchTableEntryLine(line)
                if o is None:
                    break
                table.addTableEntry(o)
                i += 1
                continue
            self.tables.append(table)

    def __str__(self):
        return json.dumps(self.tables, indent=2, default=serialize)

class Dht4():
    __slots__ = ["infile", "pendingLine", "table"]

    def __init__(self, infile):
        assert(isinstance(infile, io.TextIOWrapper))
        self.infile = infile
        self.pendingLine = None
        self.table = {}

    def readTableHeader(self):
        line = None
        if self.pendingLine is None:
            line = self.infile.readline()
        else:
            line = self.pendingLine
            self.pendingLine = None

sampleLines = """0000000000000000000000000000000000000000 count: 8 updated: 584 s ago (cached)
    Node 1410ff1c8ee412728fb297f967ba8cfa43ddfe7c 51.91.75.152:58432 updated: 14 s ago, replied: 584 s ago [good]
    Node 158ee07d251e1fbc1dd95a8cb0f88d771d838e5a 192.252.140.235:4235 updated: never
    Node 0b11f6d77542b91186695814f86dd2cdda7d3d47 51.91.75.152:36126 updated: never
    Node 09df59477d0a739a271e617cf1346004707c1c38 158.69.203.11:4248 updated: never
    Node 0c16100cb988b77aa86787200e1fbf25813729ba 96.48.243.201:5022 updated: never
    Node 02e2037cc1adfe94d34749476ceacd75e9c7494b 192.252.140.235:4249 updated: never
    Node 0441cacda5ddbc7f8d1ca8e4f083e3bccb9853af 192.252.140.236:4225 updated: never
    Node 2220e7cabf0a80b7c802e1185da8b3860a2745ab 192.252.140.236:4222 updated: 584 s ago [good]
4000000000000000000000000000000000000000 count: 8 updated: 307 s ago
    Node 4847a6816ffeb3abcb73deed17ee8039aaeb6b33 54.36.178.20:4238 updated: 307 s ago [good]
    Node 457901da1ed0f25560f95f5f18593fb833fc5506 54.36.178.20:4246 updated: 566 s ago [good]
    Node 43b53ba67090b1b81f61e31a3cddcf3403ed7ffb 67.253.17.207:5270 updated: 10.7 s ago, replied: 566 s ago [good]
    Node 40160730144edf99de5a9852db8ac93016280472 51.91.75.152:34913 updated: never
    Node 4090a86b1413702c07d841f1b672b6e8106f2898 158.69.203.51:4243 updated: never
    Node 50a37e58c63a25a9310fdee40328b1940ba1c970 192.252.140.236:4235 updated: 1.17e+03 s ago
    Node 50c94e29e4cd7549992d34eb253ec02612f4a0df 51.77.188.15:5702 updated: 566 s ago [good]
    Node 5e90112da31bb863d4ac141ac23e1afc28757c6d 192.252.140.236:4240 updated: 1.21e+03 s ago
6000000000000000000000000000000000000000 count: 8 updated: 584 s ago (cached)
    Node 640742b9bb0b2b6a3cc766556e0f0cf8bf385cbd 192.252.140.235:4251 updated: 584 s ago [good]
    Node 675d5706bf5d24e34059721a907aea581c09dfb1 51.38.40.210:4240 updated: 584 s ago [good]
    Node 678611422a166411159948717d566c7ef31acf51 158.69.203.11:4237 updated: 584 s ago [good]
    Node 64bce5fc2cede8dfdf45248adde1cb77e7a5d686 174.126.226.131:4542 updated: 584 s ago [good]
    Node 6463534768b40361cc7434229935bdd0aff28ec3 192.252.140.236:4242 updated: 584 s ago [good]
    Node 6105b7180e2ac9d2e8aacc3f8dfdc78f7e6ece48 192.252.140.235:4243 updated: 584 s ago [good]
    Node 603f136734a00086c904c2b2aae65931974ca561 134.126.153.21:8528 updated: never
    Node 6fea138bd0f7f216d0f3e0ba000b2645646508e5 54.36.178.20:4234 updated: 1.17e+03 s ago, replied: never
7000000000000000000000000000000000000000 count: 8 updated: 133 s ago (cached)
    Node 7220825608e7c1bf377959d782ce9d3e621f0e6c 192.252.140.235:4239 updated: 584 s ago [good]
    Node 711ad441c4da49c246bbae5052cc2458a4e486ad 158.69.203.11:4224 updated: 168 s ago [good]
    Node 77fa9afed4d63f1934118c340390553a39fe7a98 35.158.70.34:4222 updated: 133 s ago [good]
    Node 77138b4378a47a54484429f68a493a3125be5490 176.109.113.204:4634 updated: 836 s ago
    Node 76772d67ca90e1ed483b7bd58823d2759dde146f 81.174.246.142:4130 updated: 836 s ago
    Node 74c88e5d95d7a40925ef32256ee330016bbce8e4 158.69.203.11:4246 updated: never
    Node 75c79fb1b4207e492f363da22850aa167c8d5dda 54.36.178.20:4244 updated: 1.11e+03 s ago
    Node 76dcc2af24f859650d56fa429461445263ed7dca 54.36.178.20:40533 updated: 18.1 s ago, replied: 1.19e+03 s ago [good]
7800000000000000000000000000000000000000 count: 8 updated: 77.4 s ago
    Node 787921600412a255b9b8f8e4c65da65287cd05cb 145.255.173.7:41725 updated: 44.7 s ago, replied: never
    Node 79697a2f610c8907fcb7b826b962d029c78f1b85 2.84.34.127:7802 updated: 326 s ago, replied: never [expired]
    Node 79fc1895a1971012eee980e94313c8593b3b4dc4 86.248.221.5:4950 updated: 285 s ago, replied: never [expired]
    Node 79b76a34f722f8eac16d7e4cacf9e22fd50794d8 208.88.110.46:22334 updated: 296 s ago, replied: never [expired]
    Node 78e9db7ce7ec96efd9dbff32fe1d121040063fa1 185.209.190.186:5906 updated: 303 s ago, replied: never [expired]
    Node 78831ce2e065e249e8d82a95d62be8a4b651573d 51.254.39.157:4240 updated: 285 s ago [good]
    Node 79d8a325fdb73c7a00c2feeea3403f8e8cd17a56 134.176.205.148:6442 updated: 2.58 s ago, replied: 77.4 s ago [good]
    Node 782f2ce0e660ec96ba845cd0fbcb47c5ca969129 90.3.49.3:6590 updated: 266 s ago [good]
7a00000000000000000000000000000000000000 count: 3 updated: 34.4 s ago
    Node 7aa22520e10c69d9c5389333f9b2db97825f5eec 178.255.144.1:41617 updated: 446 s ago, replied: never [expired]
    Node 7ae9f90c775b8ad00b9924a7cc29f76938d9e007 185.45.207.55:8586 updated: 206 s ago, replied: never [expired]
    Node 7a9342f8a53650c22492014ade6da425e51f7777 65.78.148.69:5176 updated: 34.4 s ago [good]
7b00000000000000000000000000000000000000 count: 8 updated: 68.3 s ago
    Node 7bda70d57a081b9ee2c9e398e90f84ad7e6c521d 213.100.210.124:4222 updated: 67.7 s ago, replied: never
    Node 7b3ed6c72afbae994997f162138b62b431d43186 157.45.100.92:5162 updated: 3.52 s ago, replied: 68.3 s ago [good]
    Node 7b4b74ff6e25638b059772614c9c524b31d1c248 190.113.102.12:64776 updated: 143 s ago, replied: 157 s ago [good]
    Node 7b6423119ea65ee6bb14e63db84f24ef16a85d3a 86.243.163.50:1026 updated: 82.4 s ago [good]
    Node 7b4b6e9fcb57b4440bf362a949bbff95b9ffe6fc 54.36.178.20:42924 updated: 226 s ago [good]
    Node 7b2acc621f8bf5f0b2868e7e5f5cdf57935bba13 192.252.140.235:4226 updated: 239 s ago [good]
    Node 7b951679d6038ad1ec316ed449a9bd798fbb58ed 95.129.249.5:1030 updated: 133 s ago [good]
    Node 7b7ce08b4af2c40edad28c20f9567832b5ae26fb 82.228.120.14:7220 updated: 142 s ago [good]
7c00000000000000000000000000000000000000 count: 8 updated: 13.1 s ago (cached)
    Node 7c8d13a7467382eaaa0c76a02b1b8337d66e9209 94.181.196.25:37898 updated: 13.1 s ago [good]
    Node 7c43ce7cd8a0b23b173c7b3a55080aca4efd4648 51.38.40.210:4226 updated: 1.12e+03 s ago
    Node 7e207169823cfb810e334815d6c30e3054975b96 78.200.117.39:8566 updated: 827 s ago
    Node 7ff5077c950ea7f493faaf788502482f724e704e 158.69.203.11:4231 updated: 954 s ago, replied: 1.2e+03 s ago
    Node 7c24ea4712daa2d1133490d33b18eaf180c0a1e0 58.176.208.142:5662 updated: 6.47 s ago, replied: 1.06e+03 s ago [good]
    Node 7e7f7f765ecd0bb82119cd1e7168e2724738f060 192.252.140.236:4224 updated: 250 s ago [good]
    Node 7f140bd8859d802e6fc64223a3a9ba95695d3314 192.252.140.235:4236 updated: 1.2e+03 s ago
    Node 7e18d8b7f00ced8b5e9e260db1c9b0dee5c6f40a 54.36.178.20:4241 updated: 446 s ago [good]
8000000000000000000000000000000000000000 count: 8 updated: 256 s ago (cached)
    Node a8cb0a2e917ca9a15785f1fc2c984304248e1a43 51.38.40.210:4245 updated: 460 s ago [good]
    Node db0efcefae1298d04dec05f09488696a378f2bba 68.50.74.163:7854 updated: 584 s ago [good]
    Node c0f419c6c0b7be18f7c4ad32a0a3311ba5aab1e5 81.38.90.89:8070 updated: 584 s ago [good]
    Node ce82084f0dc3a9de3d2cd2c7f3382881dfc2528e 51.91.75.152:50318 updated: 104 s ago, replied: 584 s ago [good]
    Node ba15f25184410eef8899398fc4173f5853a1912b 54.36.178.20:4230 updated: 584 s ago [good]
    Node d35d33f78bde9f0a9b5211d3a2e6cecdf8831696 158.69.203.51:4222 updated: 310 s ago [good]
    Node 91a77d1af72c9e97738a0dc09bb3d3e03b2fa4c2 158.69.203.11:4222 updated: 305 s ago [good]
    Node f6802c0f8b2eee0c91a38119b3db02ca24a1e0f6 192.252.140.235:4222 updated: 256 s ago [good]"""

if __name__ == "__main__":
    lines = sampleLines.split("\n")
    routingTables = RoutingTables(lines)
    print(routingTables)

