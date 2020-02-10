#!/usr/bin/make -f 
.ONESHELL:
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

