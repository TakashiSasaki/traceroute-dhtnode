#!/usr/bin/make -f 
.ONESHELL:
.PHONY: dht

help:
	# make help
	# make dht
	# make test

test: test-matchTableEntryLine test-matchTableHeaderLine

test-matchTableEntryLine:
	python3 matchTableEntryLine.py
	
test-matchTableHeaderLine:
	python3 matchTableHeaderLine.py

test-parseDht4:
	python3 parseDht4.py 1581476326.dht4

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
	  echo Created new session $@
	  tmux send-keys -t $@  "python3 dht.py" C-m
	fi

test-ipv6:
	sudo python3 traceroute_v6.py 133.71.200.55

