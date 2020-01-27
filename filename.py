import sys, re

filename = sys.argv[1]
m = re.match("^(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d),(\d\d\d\d\d\d\d\d\d)",filename)
year = int(m[1])
month = int(m[2])
day = int(m[3])
hour = int(m[4])
minute = int(m[5])
second = int(m[6])
msecond = int(m[7])

print(year, month, day, hour, minute, second, msecond)
