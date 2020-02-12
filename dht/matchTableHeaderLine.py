sampleTableHeaderLine = "7b00000000000000000000000000000000000000 count: 8 updated: 68.3 s ago"
import re
def matchTableHeaderLine(line):
    m = re.match("^\s*([0-9a-f]+)\scount:\s([0-9]+)\supdated:\s([0-9.]+)\ss\sago", line)
    if m is None:
        return None
    tableHeader = {}
    tableHeader["mask"] = m[1]
    tableHeader["count"] = int(m[2])
    tableHeader["ago"] = float(m[3])
    return tableHeader

if __name__ == "__main__":
    tableHeader = matchTableHeaderLine(sampleTableHeaderLine)
    print(tableHeader)

