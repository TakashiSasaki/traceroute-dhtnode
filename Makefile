#!/usr/bin/make -f 
.ONESHELL:
help:
	#

test-ipv6:
	sudo python3 traceroute_v6.py 133.71.200.55

