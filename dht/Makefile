#!/usr/bin/make -f 
.ONESHELL:
.PHONY: dht

help:
	# make help
	# make dht
	# make test

test: test-TableEntry test-TableHeader test-RoutingTables  test-RoutingTablesLog
test-HelloLogger:
	python3 HelloLogger.py

test-CheckEpoch:
	python3 CheckEpoch.py

test-RoutingTablesLog:
	cd dht
	python3 ../RoutingTablesLog.py 1581655166.dht4
	python3 ../RoutingTablesLog.py 1581655166.dht6

test-RoutingTables:
	python3 RoutingTables.py dht/1581498637.dht4 | jq
	python3 RoutingTables.py dht/1581498637.dht6 | jq

test-dht:
	python3 dht.py --dry-run

test-RoutingTable:
	python3 RoutingTable.py
	
test-TableHeader:
	python3 TableHeader.py

	
test-TableEntry:
	python3 TableEntry.py

test-parseDht4:
	python3 parseDht4.py dht/1581476326.dht4

%.json: %.dht4
	python3 parseDht4.py <$< >$@
	#
	
%.json: %.dht6
	python3 parseDht6.py <$< >$@
	#	

dht:
	@
	tmux kill-session -t $@
	TMUX= tmux new-session -d -s $@
	if [ $$? -eq 0 ]; then
	  -mkdir dht
	  echo Created new session $@
	  tmux send-keys -t $@  "python3 dht.py -c 0 -i 1800 -s dht" C-m
	fi

test-ipv6:
	sudo python3 traceroute_v6.py 133.71.200.55

