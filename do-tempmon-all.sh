#!/bin/bash -x

# do-tempmon-all.sh
# Gathers sensor data on multiple machines, according to host file
#
# Created by: Giacomo Mc Evoy - giacomo@lncc.br
# LNCC 2015

# Calculate directory local to script and load configuration
LOCAL_DIR="$( cd "$( dirname "$0" )" && pwd )"
source $LOCAL_DIR/config

mkdir $OUTPUT_DIR

# begin endless loop (can be killed with process PID)
while [ '1' == '1' ]
do 
	# register collection
	TIMESTAMP=$(date +"$DATE_FORMAT")
	echo "Monitoring hosts at ${TIMESTAMP}"

	# iterate each host
	for HOST in $(cat $HOST_FILE)
	do 
		# calculate CSV output file
		CSV_FILE="${OUTPUT_DIR}/${HOST}.csv"

		# collect sensor data of host to CSV
		$LOCAL_DIR/do-tempmon-single.sh $HOST $CSV_FILE
	done

	# wait for next collection
	sleep $SENSOR_INTERVAL
done