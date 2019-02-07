default: $(addsuffix .ipv6-addresses,$(basename $(wildcard *.dhtnode-routing-table-v6))) \
	all.ipv6-addresses

test-ipv6:
	sudo python3 traceroute_v6.py 133.71.200.55


%.ipv6-addresses: %.dhtnode-routing-table-v6
	cat $< | sed -n -r -e "s/.+ \[([0-9a-f:]+)\]:[0-9]+ age.+/\1/p" | sort -u | tee $@

all.ipv6-addresses: $(addsuffix .ipv6-addresses,$(basename $(wildcard *.dhtnode-routing-table-v6)))
	cat $^ | sort -u | tee $@
