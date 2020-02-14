#!/usr/bin/python3

def CheckEpoch():
    import os, time, subprocess
    epochByDateCommand = int(subprocess.check_output(["date", "+%s"]))
    print(epochByDateCommand)
    epochByTimeFunction = int(time.time())
    print(epochByTimeFunction)
    assert(epochByDateCommand == epochByTimeFunction)

if __name__ == "__main__":
    CheckEpoch()

