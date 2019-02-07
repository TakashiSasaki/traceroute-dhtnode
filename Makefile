.PHONY: default v4 v6

default: $(addsuffix .ipv6-addresses,$(basename $(wildcard *.dhtnode-routing-table-v6))) \
	all.ipv6-addresses

v4:
	-mkdir v4
	for i in {0..9}; do (cd v4; python3 ../dht_v4.py); sleep 10; done

v6:
	-mkdir v6
	for i in {0..9}; do (cd v6; python3 ../dht_v6.py); sleep 10; done

test-ipv6:
	sudo python3 traceroute_v6.py 133.71.200.55


%.ipv6-addresses: %.dhtnode-routing-table-v6
	cat $< | sed -n -r -e "s/.+ \[([0-9a-f:]+)\]:[0-9]+ age.+/\1/p" | sort -u | tee $@

all.ipv6-addresses: $(addsuffix .ipv6-addresses,$(basename $(wildcard *.dhtnode-routing-table-v6)))
	cat $^ | sort -u | tee $@

.PHONY: ipv6-address
ipv6-address: all.ipv6-addresses
	cat $< | while read line; do\
		x=`echo -n $${line} | md5sum | sed -n -r -e "s/^([0-9a-f]+) .*$$/\1/p"` ;\
		echo $${line} >$${x}.ipv6-address;\
	done

%.ipv6-ping: %.ipv6-address
	ping6 -c 5 $(shell cat $<) | tee -a $@

.PHONY: ipv6-ping
ipv6-ping: $(addsuffix .ipv6-ping,$(basename $(wildcard *.ipv6-address)))
