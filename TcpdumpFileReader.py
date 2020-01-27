#!/usr/bin/python3
import sys, re

class TcpdumpFileReaderError(RuntimeError):
    pass

class TcpdumpFileReader:

    __slots__ = ["file", "bufferedLine"]

    def __init__(self, file):
        self.file = file
        self.bufferedLine = None

    def peekLine(self):
        if self.bufferedLine is not None:
            return self.bufferedLine
        line = self.file.readline()
        if len(line) == 0:
            raise TcpdumpFileReaderError
        self.bufferedLine = line
        return line

    def getLinesPerPacket(self):
        firstLine = self.peekLine()
        firstLineMatch  = re.match("^[0-9].+", firstLine)

        if firstLineMatch is None:
            raise TcpdumpFileReaderError

        lines = [firstLine]
        self.bufferedLine = None

        while True:
            try:
                trailingLine = self.peekLine()
                trailingLineMatch = re.match("^[0-9].+", trailingLine)
                if trailingLineMatch is None:
                    lines.append(self.bufferedLine)
                    self.bufferedLine = None
                else:
                    return lines
            except TcpdumpFileReaderError:
                return lines

if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename)
    tcpdumpFileReader = TcpdumpFileReader(file)

    while True:
        try:
            print("---- start of a packet")
            lines = tcpdumpFileReader.getLinesPerPacket()
            print(lines)
            print("---- end of a packet")
        except TcpdumpFileReaderError:
            print("---- end of the file ----")
            break

