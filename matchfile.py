#!/usr/bin/python3
from TcpdumpFileReader import TcpdumpFileReader as TFR
import sys, re

class UnknownPacketTypeError(RuntimeError):
    pass

#ICMP udp port
def matchicmp1(lines):
    if len(lines) != 4:
        return False
    m1_1 = re.match("([0-9.:]+)\sIP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[none],\sproto\sICMP\s(([0-9]+)),\slength\s([0-9]+))", lines[0])
    m1_2 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sICMP\shost\s([0-9.]+)\sunreachable,\slength\s([0-9]+)", lines[1])
    m1_3 = re.match("IP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags[DF],\sproto\sUDP\s(([0-9]+)),\slength\s([0-9]+))", lines[2])
    m1_4 = re.match("([0-9.]+)\s>\s([0-9.:])\sUDP,\slength\s([0-9]+)", lines[3])
    if m1_1 is None or m1_2 is None or m1_3 is None or m1_4 is None:
        return False        
    print("lines matched in matchicmp1")
    return True

#icmp echo
def matchicmp2(lines):
    if len(lines) != 2:
        return False
    m2_1 = re.match("([0-9.:]+)\sIP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[DF],\sproto\sICMP\s(([0-9]+)),\slength\s([0-9]+))",lines[0])
    m2_2 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sICMP\secho\sreply,\sid\s([0-9]+),\sseq\s([0-9]+),\slength\s([0-9]+)",lines[1])
    if m2_1 is None or m2_2 is None:
        return False
    print("lines matched in matchicmp2.")
    return True

#unreachable
def matchicmp3(lines):
    if len(lines) != 4:
        return False
    m3_1 = re.match("([0-9.]+)\sIP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[none],\sproto\sICMP\s(1),\slength\s([0-9]+))",lines[0])
    m3_2 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sICMP\shost\s([0-9.]+)\sunreachable,\slength\s([0-9]+)",lines[1])
    m3_3 = re.match("IP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[DF],\sproto\sUDP\s(([0-9]+)),\slength\s([0-9]+))",lines[2])
    m3_4 = re.match("([0-9.]+)\s>\s([0-9.:])\sUDP,\slength\s([0-9]+)",lines[3])
    if m3_1 is None or m3_2 is None or m3_3 is None or m3_4 is None:
        return False
    print("Lines matched in matchicmp3.")
    return True

#unreachable - admin
def matchicmp4(lines):
    if len(lines) != 4:
        return False
    m4_1 = re.match("([0-9.]+)\sIP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[none],\sproto\sICMP\s(1),\slength\s([0-9]+))",lines[0])
    m4_2 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sICMP\shost\s([0-9.]+)\sunreachable\s-\sadmin\sprohibited,\slength\s([0-9]+)",lines[1])
    m4_3 = re.match("IP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[DF],\sproto\sUDP\s(([0-9]+)),\slength\s([0-9]+))",lines[2])
    m4_4 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sUDP,\slength\s([0-9]+)",lines[3])
    if m4_1 is None or m4_2 is None or m4_3 is None or m4_4 is None:
        return False
    print("Lines matched in matchicmp4.")
    return True

#time exceeded
def matchicmp5(lines):
    if len(lines) != 7:
        return False
    m5_1 = re.match("([0-9.]+)\sIP\s(tos\s0x0,\sttl([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[DF],\sproto\sICMP\s(([0-9]+)),\slength\s([0-9]+))",lines[0])
    m5_2 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sICMP\stime\sexceeded\sin-tracsit,\slength\s([0-9]+)",lines[1])
    m5_3 = re.match("IP\s(tos\s0x0,\sttl\s([0-9]+),\sid\s([0-9]+),\soffset\s0,\sflags\s[DF],\sproto\sUDP\s(([0-9]+)),\slength\s([0-9]+)",lines[2])
    m5_4 = re.match("([0-9.]+)\s>\s([0-9.:]+)\sUDP,\slength\s([0-9]+)",lines[3])
    m5_5 = re.match("MPLS\sextension\sv2,\schecksum\s\w\w\w\w\w\w\s(correct),\slength\s([0-9]+)",lines[4])
    m5_6 = re.match("MPLS\sStack\sEntry\sObject\s(1),\sClass-Type:\s1,\slength\s([0-9]+)",lines[5])
    m5_7 = re.match("label\s([0-9]+),\sexp\s0,\s[S],\sttl\s([0-9]+)",lines[6])
    if m5_1 is None or m5_2 is None or m5_3 is None or m5_4 is None or m5_5 is None or m5_6 is None or m5_7 is None:
        return False
    print("Lines matched in matchicmp5.")
    return True

if __name__ == "__main__":
    file = open(sys.argv[1])
    tfr = TFR(file)
    print(tfr)
    while True:
        try:
            lines = tfr.getLinesPerPacket()
            #if len(lines) == 0:
            #    raise RuntimeError("no lines in a block")
            if matchicmp1(lines):
                continue
            if matchicmp2(lines):
                continue
            if matchicmp3(lines):
                continue
            if matchicmp4(lines):
                continue
            if matchicmp5(lines):
                continue
            else:
                raise UnknownPacketTypeError

        except RuntimeError:
            break;
        pass

    print("finished")

