sampleTableHeaderLine = "7b00000000000000000000000000000000000000 count: 8 updated: 68.3 s ago"
import re,json

class TableHeaderException(RuntimeError):
    pass

class TableHeader():
    __slots__ = ["tableHeader"]

    def __init__(self):
        self.tableHeader = None

    def read(self, lines):
        m = re.match("^\s*([0-9a-f]+)\scount:\s([0-9]+)\supdated:\s([0-9.]+)\ss\sago", lines[0])
        if m is None:
            raise TableHeaderException(lines[0])
        self.tableHeader = {}
        self.tableHeader["mask"] = m[1]
        self.tableHeader["count"] = int(m[2])
        self.tableHeader["ago"] = float(m[3])
        return lines[1:]

class TableHeaderEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, TableHeader):
            return obj.tableHeader
        return json.JSONEncoder.default(self, obj)

if __name__ == "__main__":
    tableHeader = TableHeader()
    tableHeader.read([sampleTableHeaderLine])
    print(json.dumps(tableHeader, cls=TableHeaderEncoder))

