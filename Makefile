.ONESHELL:


help:
	# sudo make all
	# make rename

rename: FORCE
	find -type f -name "*pcap*" -exec rename-to-iso8601 {} \;

all: FORCE rename
	tcpdump -G 86400 -C 1 -w icmp/icmp.pcap -z rename-to-iso8601 icmp &
	tcpdump -G 86400 -C 1 -w tcp7/tcp7.pcap -z rename-to-iso8601 tcp port 7 &
	tcpdump -G 86400 -C 1 -w tcp9/tcp9.pcap -z rename-to-iso8601 tcp port 9 &
	tcpdump -G 86400 -C 1 -w tcp80/tcp80.pcap -z rename-to-iso8601 tcp port 80 &
	tcpdump -G 86400 -C 1 -w tcp443/tcp443.pcap -z rename-to-iso8601 tcp port 443 &
	tcpdump -G 86400 -C 1 -w tcp5001/tcp5001.pcap -z rename-to-iso8601 tcp port 5001 &
	tcpdump -G 86400 -C 1 -w udp7/udp7.pcap -z rename-to-iso8601 udp port 7 &
	tcpdump -G 86400 -C 1 -w udp9/udp9.pcap -z rename-to-iso8601 udp port 9 &
	tcpdump -G 86400 -C 1 -w udp53/udp53.pcap -z rename-to-iso8601 udp port 53 &
	tcpdump -G 86400 -C 1 -w udp123/udp123.pcap -z rename-to-iso8601 udp port 123 &
	tcpdump -G 86400 -C 1 -w udp80/udp80.pcap -z rename-to-iso8601 udp port 80 &
	tcpdump -G 86400 -C 1 -w udp443/udp443.pcap -z rename-to-iso8601 udp port 443 

FORCE:
