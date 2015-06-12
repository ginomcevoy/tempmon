#!/bin/bash

# tempmon-start.sh
# Starts monitoring of multiple machines.
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

# Start monitoring, save process PID to kill process with stop script
nohup $LOCAL_DIR/do-tempmon-all.sh > $LOG_FILE 2>&1 & echo $! > $PID_FILE