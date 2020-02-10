#!/usr/bin/make -f 

dht:
	python3  DhtRoutingTableLogger.py

test-ipv6:
	sudo python3 traceroute_v6.py 133.71.200.55

