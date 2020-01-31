#!/usr/bin/python3
from TcpdumpFileReader import TcpdumpFileReader as TFR
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
            #ICMP udp port
            m1_1 = re.match("([0-9.:]+)\sIP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[none],\sproto\sICMP\s(([0-9]+)),\slength\s([0-9]+))", lines[0])
            if m1_1 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m1_2 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sICMP\shost\s([0-9.]+)\sunreachable,\slength\s([0-9]+)", lines[1])
            if m1_2 is not None:
                pass
            else: 
                raise UnknownPacketTypeError
            m1_3 = re.match("IP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags[DF],\sproto\sUDP\s(([0-9]+)),\slength\s([0-9]+)", lines[2])
            if m1_3 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m1_4 = re.match("([0-9.]+)\s>\s([0-9.:])\sUDP,\slength\s([0-9]+)", lines[3])
            if m1_4 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            if(len(lines) > 4):
                raise UnknownPacketTypeError
            continue
            #ICMP echo
            m2_1 = re.match("([0-9.:]+)\sIP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[DF],\sproto\sICMP\s(([0-9]+)),\slength\s([0-9]+))",lines[0])
            if m2_1 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m2_2 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sICMP\secho\sreply,\sid\s([0-9]+),\sseq\s([0-9]+),\slength\s([0-9]+)",lines[1])
            if m2_2 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            if(len(lines) > 2):
                raise UnknownPacketTypeError
            continue
            #ICMP host
            m3_1 = re.match("([0-9.:]+)\sIP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[none],\sproto\sICMP\s(([0-9]+)),\slength\s([0-9]+))",lines[0])
            if m3_1 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m3_2 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sICMP\shost\s([0-9.]+)\sunreachable,\slength\s([0-9]+)",lines[1])
            if m3_2 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m3_3 = re.match("IP\s(tos\s0x0,\sttl([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[DF],\sproto\sUDP\s(([0-9]+)),\slength\s([0-9]+)",lines[2])
            if m3_3 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m3_4 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sUDP,\slength\s([0-9]+)",lines[3])
            if m3_4 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            if(len(lines) > 4):
                raise UnknownPacketTypeError
            continue
            #unreachable - admin prohibited filter
            m4_1 = re.match("([0-9.:]+)\sIP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[none],\sproto\sICMP\s(([0-9]+)),\slength\s([0-9]+))",lines[0])
            if m4_1 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m4_2 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sICMP\shost\s([0-9.]+)\sunreachable\s-\sadmin\sprohibited\sfilter,\slength([0-9]+)",lines[1])
            if m4_2 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m4_3 = re.match("IP\s(tos\s0x0,\sttl([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[DF],\sproto\sUDP\s(([0-9]+)),\slength\s([0-9]+)",lines[2])
            if m4_3 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m4_4 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sUDP,\slength\s([0-9]+)",lines[3])
            if m4_4 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            if(len(lines) > 4):
                raise UnknownPacketTypeError
            continue
            #time exceeded
            m5_1 = re.match("([0-9.:]+)\sIP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[DF],\sproto\sICMP\s(([0-9]+)),\slength\s([0-9]+))",lines[0])
            if m5_1 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m5_2 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sICMP\stime\sexceeded\sin-transit,\slength\s([0-9]+)",lines[1])
            if m5_2 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m5_3 = re.match("IP\s(tos\s0x0\s,\sttl([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[DF],\sproto\sUDP\s(([0-9]+)),\slength\s([0-9]+)",lines[2])
            if m5_3 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m5_4 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sUDP,\slength\s([0-9]+)",lines[3])
            if m5_4 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m5_5 = re.match("MPLS\sextension\sv2,\schecksum\s([a-z0-9]+)\s(correct),\slength\s([0-9]+)",lines[4])
            if m5_5 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m5_6 = re.match("MPLS\sStack\sEntry\sObject\s(1),\sClass-Type:\s1,\slength([0-9]+)",lines[5])
            if m5_6 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            m5_7 = re.match("label\s([0-9]+),\sexp\s0,\s[S],\sttl\s([0-9]+)",lines[6])
            if m5_7 is not None:
                pass
            else:
                raise UnknownPacketTypeError
            if(len(lines) > 6):
                raise UnknownPacketTypeError
            continue

        except RuntimeError:
            break;
        pass

    print(m5_1)
