.ONESHELL:
TMUX_SESSION_NAME=mainsession

help: list
	@echo
	echo ------- TARGETS ------------------------------------
	echo make dhtnode
	echo make tcpdump
	echo

list:
	@
	echo 
	echo --- LIST OF TMUX SESSIONS ----------------------
	tmux list-sessions
	echo
	#echo --- LIST OF TMUX WINDOWS IN CURRENT SESSION ----
	#tmux list-windows

choose:
	@
	tmux choose-session

tcpdump: icmp icmp6 udp7 udp9 udp53 udp4222 tcp7 tcp9 tcp80 tcp443

icmp:
	@
	tmux kill-session -t $@
	TMUX= tmux new-session -d -s $@
	if [ $$? -eq 0 ]; then
	  echo Created new session $@
	  tmux send-keys -t $@  "tcpdump -i any -n -v -tt -G 86400 -z bzip2 -w $@-%Y-%m-%dT%H:%M:%SZ.pcap icmp" C-m
	fi

icmp6:
	@
	tmux kill-session -t $@
	TMUX= tmux new-session -d -s $@
	if [ $$? -eq 0 ]; then
	  echo Created new session $@
	  tmux send-keys -t $@  "tcpdump -i any -n -v -tt -G 86400 -z bzip2 -w $@-%Y-%m-%dT%H:%M:%SZ.pcap icmp6" C-m
	fi

udp7:
	tmux kill-session -t $@
	TMUX= tmux new-session -d -s $@
	if [ $$? -eq 0 ]; then
	  echo Created new session $@
	  tmux send-keys -t $@  "tcpdump -i any -n -v -tt -G 86400 -z bzip2 -w $@-%Y-%m-%dT%H:%M:%SZ.pcap udp port 7" C-m
	fi

udp9:
	tmux kill-session -t $@
	TMUX= tmux new-session -d -s $@
	if [ $$? -eq 0 ]; then
	  echo Created new session $@
	  tmux send-keys -t $@  "tcpdump -i any -n -v -tt -G 86400 -z bzip2 -w $@-%Y-%m-%dT%H:%M:%SZ.pcap udp port 9" C-m
	fi

udp53:
	tmux kill-session -t $@
	TMUX= tmux new-session -d -s $@
	if [ $$? -eq 0 ]; then
	  echo Created new session $@
	  tmux send-keys -t $@  "tcpdump -i any -n -v -tt -G 86400 -z bzip2 -w $@-%Y-%m-%dT%H:%M:%SZ.pcap udp port 53" C-m
	fi

udp4222:
	tmux kill-session -t $@
	TMUX= tmux new-session -d -s $@
	if [ $$? -eq 0 ]; then
	  echo Created new session $@
	  tmux send-keys -t $@  "tcpdump -i any -n -v -tt -G 86400 -z bzip2 -w $@-%Y-%m-%dT%H:%M:%SZ.pcap udp port 4222" C-m
	fi
tcp7:
	tmux kill-session -t $@
	TMUX= tmux new-session -d -s $@
	if [ $$? -eq 0 ]; then
	  echo Created new session $@
	  tmux send-keys -t $@  "tcpdump -i any -n -v -tt -G 86400 -z bzip2 -w $@-%Y-%m-%dT%H:%M:%SZ.pcap tcp port 7 and 'tcp[13] & 2' != 0" C-m
	fi

tcp9:
	tmux kill-session -t $@
	TMUX= tmux new-session -d -s $@
	if [ $$? -eq 0 ]; then
	  echo Created new session $@
	  tmux send-keys -t $@  "tcpdump -i any -n -v -tt -G 86400 -z bzip2 -w $@-%Y-%m-%dT%H:%M:%SZ.pcap tcp port 9 and 'tcp[13] & 2' != 0" C-m
	fi

tcp80:
	tmux kill-session -t $@
	TMUX= tmux new-session -d -s $@
	if [ $$? -eq 0 ]; then
	  echo Created new session $@
	  tmux send-keys -t $@  "tcpdump -i any -n -v -tt -G 86400 -z bzip2 -w $@-%Y-%m-%dT%H:%M:%SZ.pcap tcp port 80 and 'tcp[13] & 2' != 0" C-m
	fi

tcp443:
	tmux kill-session -t $@
	TMUX= tmux new-session -d -s $@
	if [ $$? -eq 0 ]; then
	  echo Created new session $@
	  tmux send-keys -t $@  "tcpdump -i any -n -v -tt -G 86400 -z bzip2 -w $@-%Y-%m-%dT%H:%M:%SZ.pcap tcp port 443 and 'tcp[13] & 2' != 0" C-m
	fi

tmux-bash-window:
	@
	TMUX_WINDOW_NAME=bash-window
	TMUX_COMMAND=bash
	tmux list-windows -t $(TMUX_SESSION_NAME) | cut -f 2 -d " " | grep $${TMUX_WINDOW_NAME} 
	if [ $$? -eq  0 ] ; then
	   echo tmux $(TMUX_SESSION_NAME):$${TMUX_WINDOW_NAME} already exists.
	   tmux list-windows -t $(TMUX_SESSION_NAME)
	   exit
	fi
	tmux new-window -P -d -k -n $${TMUX_WINDOW_NAME} -t $(TMUX_SESSION_NAME) $${TMUX_COMMAND}
	tmux has-session -t $(TMUX_SESSION_NAME):$${TMUX_WINDOW_NAME}
	if [ $$? -eq  0 ] ; then
	   echo tmux $(TMUX_SESSION_NAME):$${TMUX_WINDOW_NAME} has created.
	fi
	tmux list-window -t $(TMUX_SESSION_NAME)

FORCE:

