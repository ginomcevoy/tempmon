#!/bin/bash

# tempmon-stop.sh
# Stop monitoring of multiple machines.
# Relevant files:
# config: configuration file with parameters
# hosts: file with hosts to monitor, should be translatable to IP addresses
# reachable via IPMI.
#
# Created by: Giacomo Mc Evoy - giacomo@lncc.br
# LNCC 2015

# Calculate directory local to script and load configuration
LOCAL_DIR="$( cd "$( dirname "$0" )" && pwd )"
source $LOCAL_DIR/config

# Stop monitoring by killing the main process and its children (each host call)
PID=$(cat $PID_FILE)
pkill -TERM -P $PID && kill -TERM $PID

rm $PID_FILE