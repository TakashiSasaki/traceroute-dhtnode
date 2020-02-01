#!/usr/bin/python3
import pymysql.cursors
import sys, re
import datetime
import os

target_dir = '/home/terao/opendht-data/v4/temp'

file_list = os.listdir(target_dir)

for i in range(len(file_list)):
    if os.path.isdir(target_dir + '/' + file_list[i]):
        continue
    if file_list[i].split('.')[-1]!='txt':
        continue


filename = sys.argv[1]
m = re.match("^(\d\d\d\d)(\d\d)(\d\d)_(\d\d)(\d\d)(\d\d)v.+",filename)
year = int(m[1])
month = int(m[2])
day = int(m[3])
hour = int(m[4])
minute = int(m[5])
second = int(m[6])

dt = datetime.datetime(year, month, day, minute, second, 0, tzinfo=None)
print(dt)

conn = pymysql.connect(host="localhost",user="terao",db="opendht",password="unit313242")
sql = "INSERT INTO opendht_test(node,IP,port,timer,datetime)VALUES(%s,%s,%s,%s,%s)"

f = open(filename, "r")
for line in f:
    m = re.match("^\s*Node([0-9a-f]{40}\s+[0-9.]+):([0-9]+)\D+(\d+).*",line)
    if m is None:continue
    if m.groups() is None:
        continue
    if len(m.groups())!=4:
        continue

    col_node = m[1]
    col_IP = m[2]
    col_port = int(m[3])
    col_rimer = int(m[4])
    col_datetime = dt

    print([col_node, col_IP, col_port, col_timer, col_datetime.isoformat()])

    cursor = conn.cursor()
    cursor.execute(sql,(col_node, col_IP, col_port, col_timer, col_datetime))

    conn.commit()
    #print([year, month, day, hour, minute, second])
