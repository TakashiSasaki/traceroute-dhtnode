.ONESHELL:
.SHELL=/bin/bash
STEM=pcap-
EXPRESSON=
.PHONY: rename help
.PRECIOUS: %.pcap

help:
	#
	# make tcpdump : 
	#  captures all ICMP, TCP with SYN flag, UDP port 7, 9, 53, 67, 68, 69, 123, 5353 or 5355.
	#  It requires root permission.
	#
	# make rename : 
	#  renames all *.[1-9] files to *.pcap.
	#  Each stem is its last modified time in ISO 8601 style.
	#
	# make hoge.pcap: 
	#  runs tcpdump with the expression in hoge.filter.
	#  It requires root permission.
	#  

rename: 
	for x in  *.pcap[123456789]
	do
	DATETIMESTRING=`date +%Y%m%dT%H%M%S -r $${x}`
	echo $${DATETIMESTRING}
	mv $${x} $${DATETIMESTRING}.pcap
	echo $${x}
	done

%.pcap : %.filter
	-tcpdump -C 1 -w $@ `cat $<`

tcpdump:
	-tcpdump -nn -G 3600 -w %FT%T.pcap icmp or udp port 7 or udp port 9 or udp port 53 or udp portrange 67-69 or udp port 123 or 4222 or 5353 or 5355 or tcp[tcpflags] \& tcp-syn != 0 

