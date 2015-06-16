#!/bin/bash

# tempmon-status.sh
# Indicates status for the execution of Tempmon
# Relevant files:
# config: configuration file with parameters
#
# Created by: Giacomo Mc Evoy - giacomo@lncc.br
# LNCC 2015

# Calculate directory local to script and load configuration
LOCAL_DIR="$( cd "$( dirname "$0" )" && pwd )"
source $LOCAL_DIR/config

# Check for PID file
if [[ -f $PID_FILE ]]; then

	# Check for PID process
	PID=$(cat $PID_FILE)
	ps -fea | grep $PID | grep -v grep &> /dev/null
	if [[ $? -eq 0 ]]; then
		echo "Tempmon is running with PID $PID."
	else
		# PID file is present but process not found
		>&2 echo "ERROR: PID file for Tempmon present, but Tempmon process not found (probably was killed)."
		exit 1
	fi
else
	echo "Tempmon is not running (PID file not present)."
fi