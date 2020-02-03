from TcpdumpFileReader import TcpdumpFileReader as TFR, TcpdumpFileReaderError
import sys, re

class UnknownPacketTypeError(RuntimeError):
    pass

if __name__ == "__main__":
    file = open(sys.argv[1])
    tfr = TFR(file)
    print(tfr)
    while True:
        try:
            lines = tfr.getLinesPerPacket()
            #if len(lines) == 0:
            #    raise RuntimeError("no lines in a block")
            m11 = re.match("([0-9.:]+)\sIP\s(tos\s0x0,\sttl\s([0-9]+))", line[0])
            if m11 is not None:
                m12 = re.match("1.*", line[1])
                if m12 is not None:
                    pass
                else:
                    raise UnknownPacketTypeError
                m13 = re.match(".*", line[2])
                if m13 is not None:
                    pass
                else:
                    raise UnknownPacketTypeError
                m14 = re.match(".*", line[3])
                if m14 is not None:
                    pass
                else:
                    raise UnknownPacketTypeError
                if(len(lines) > 4):
                    raise UnknownPacketTypeError
                # insert a record here
                continue
            m21 = re.match("hogehoge")
            if m21 is not None:
                pass
            raise UnknownPacketTypeError
        except TcpdumpReaderError:
            break;
