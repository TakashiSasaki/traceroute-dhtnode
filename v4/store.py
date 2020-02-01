#!/usr/bin/python3
import pymysql.cursors
import sys,re
import datetime

#    Node 32d78c90c53c7773dd3d655f5919331036e2da5a 158.69.203.11:4250 age 477 [good]

filename = sys.argv[1]
print(filename)
m = re.match("^(\d\d\d\d)(\d\d)(\d\d)_(\d\d)(\d\d)(\d\d)v.+", filename)
year = int(m[1])
month = int(m[2])
day = int(m[3])
hour = int(m[4])
minute = int(m[5])
second = int(m[6])

dt = datetime.datetime(year, month, day, hour, minute, second, 0, tzinfo=None)
print(dt)

conn = pymysql.connect(host="localhost", user="terao", db="opendht")
sql = "INSERT INTO opendhtv4  (node,IP,port,timer,datetime) VALUES(%s,%s,%s,%s,%s)"

f = open(filename, "r")
for line in f:
    #print(line.strip())
    m = re.match("^\s*Node ([0-9a-f]{40})\s+([0-9.]+):([0-9]+) \D+(\d+).*",
line)
    if m is None: continue
    if m.groups() is None: continue
    if len(m.groups())!= 4: continue

    col_node = m[1]
    col_IP = m[2]
    col_port = int(m[3])
    col_timer = int(m[4])
    col_datetime = dt

    print([col_node, col_IP, col_port, col_timer, col_datetime.isoformat()])

    cursor = conn.cursor()
    cursor.execute(sql, (col_node, col_IP, col_port,col_timer,
col_datetime))

    conn.commit()
    #print([year, month, day, hour, minute, second])
