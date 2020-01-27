#!/usr/bin/python3
import pymysql.cursors
import sys, re
import datetime

filename = sys.argv[1]
m = re.match("^(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d),(\w\w\w\w\w\w)", filename)
year = int(m[1])
month = int(m[2])
day = int(m[3])
hour = int(m[4])
minute = int(m[5])
second = int(m[6])
msecond = int(m[7])

dt = datetime.datetime(year, month, day, hour, minute, second, msecond)
print(dt)

conn = pymysql.connect(host="localhost", user="terao", db="opendht")
sql = "INSERT INTO icmp(sendIP,recvIP,icmp,UDPport,length,datetime) VALUES(%s,%s,%s,%s,%s,%s)"

f = open(filename, "r")
for line in f:
    #print(line.strip())
    m = re.match("\d\sIP\s([0-9.]+)\s>\s([0-9.:]+)\sICMP\s([0-9.]+)\sudp\sport\s([0-9]+)\sunrechable,\slendth([0-9]+)",line)
    if m is None: continue
    if m.groups() is None: continue
    if len(m.groups()) != 5: continue

    col_sendIP = int(m[1])
    col_recvIP = int(m[2])
    col_icmp = int(m[3])
    col_UDPport = int(m[4])
    col_length = int(m[5])
    col_datetime = dt

    print([col_sendIP, col_recvIP, col_icmp, col_UDPport, col_length, col_datetime.isoformat()])

    cursor = conn.cursor()
    cursor.execute(sql, (col_sendIP, col_recvIP, col_icmp, col_UDPport, col_length, col_datetime))
    conn.commit()
