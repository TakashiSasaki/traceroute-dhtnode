#!/bin/bash
set -u
SESSION_NAME=dhtnode
tmux kill-session -t $SESSION_NAME
sett -e
TMUX= tmux new-session -d -s $SESSION_NAME
if [ $? -eq 0 ]; then
  echo Created new session $SESSION_NAME
  echo Running dhtnode with bootstrap.ring.cx as a bootstrap node.
  tmux send-keys -t $SESSION_NAME "dhtnode -p 4222 -b bootstrap.ring.cx:4222" C-m
  echo Waiting five seconds for initial routing table.
  sleep 5
  tmux send-keys -t $SESSION_NAME "lr" C-m
fi
echo Choose the session by "'tmux choose-session'".

