import pymysql.cursors
import sys,re
import datetime

filename = sys.argv[1]

conn = pymysql.connect(host="localhost", user="terao", db="opendht", password="unit313242")
sql = "INSERT INTO icmp  (time,sendIP,recvIP,echo,id,seq,length) VALUES(%s,%s,%s,%s,%s,%s,%s)"

f = open(filename, "r")
for line in f:
    #print(line.strip())
    m = re.match("^\s([0-9.])+([0-9.]+)([0-9.]+):([a-z]+)([0-9]+)([0-9]+)([0-9]+)",line)
    if m is None: continue
    if m.groups() is None: continue
    if len(m.groups())!= 7: continue

    col_time = m[1]
    col_sendIP = int(m[2])
    col_recvIP = int(m[3])
    col_echo = m[4]
    col_id = int(m[5])
    col_seq = int(m[6])
    col_length = int(m[7])

    print([col_time, col_sendIP, col_recvIP, col_echo, col_id, col_seq, col_length.isoformat()])

    cursor = conn.cursor()

    cursor.execute(sql,(col_time, col_sendIP, col_recvIP, col_echo, col_id, col_seq, col_length))

    conn.commit()
