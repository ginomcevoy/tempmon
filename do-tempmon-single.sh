#!/bin/bash -x

# do-tempmon-single.sh
# Uses ipmitool in a single machine, appends relevant 
# data to local CSV file
#
# Parameters:
# hostname: hostname of target machine
# csvFile: output file of sensor data
#
# Created by: Giacomo Mc Evoy - giacomo@lncc.br
# LNCC 2015

# Verify arguments
if [ $# -lt 2 ]; then
	>&2 echo "Uses ipmitool in a single machine, appends relevant"
	>&2 echo "data to local CSV file"
	>&2 echo 
	>&2 echo "Usage: $0 <hostname> <csvFile>"
	exit 1
fi

HOST=$1
CSV_FILE=$2

# Calculate directory local to script and load configuration
LOCAL_DIR="$( cd "$( dirname "$0" )" && pwd )"
source $LOCAL_DIR/config

# Get timestamp for call
TIMESTAMP=$(date +"$DATE_FORMAT")

# Issue ipmitool call
TEMP_FILE=/tmp/$HOST-tempmon.out
ipmitool -I lanplus -H $HOST -U $BMC_USER -P $BMC_PASS sensor > $TEMP_FILE

# Call script that parses output and appends to CSV
python $LOCAL_DIR/tempmon.py $TEMP_FILE "$TIMESTAMP" $CSV_FILE