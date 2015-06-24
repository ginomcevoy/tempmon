# tempmon
Distributed Temperature Monitor using IPMI

## Requirements:
- ipmi-tools on the head server
- Python 2.6+ on the head server
- The head server must be able to reach the nodes via an IPMI address

## Usage:
- ``./tempmon-start.sh``: start monitoring the nodes
- ``./tempmon-stop.sh``: stop monitoring the nodes
- ``./tempmon-status.sh``: query the state of Tempmon
- ``./test.sh`` for unit tests

## Configuration:
- ``hosts`` file: list the hostnames or IP addresses of the nodes to monitor. If using hostnames, these should be resolved via the ``/etc/hosts`` file.
- ``config`` file: Holds Tempmon parameters. Main parameters:
  - ``SENSOR_INTERVAL``: frequency of monitoring, in seconds (default: 3600 seconds / 1 hour)
  - ``OUTPUT_DIR``: directory that will hold output data (default: ``$HOME/ipmi-data``)
  - ``HOST_FILE``: indicates host file to read (default: ``hosts``)

## Output:
- One CSV file is generated for each node, in the directory indicated by ``OUTPUT_DIR`` parameter in the ``config`` file.
- CSV Format: 

| timeStamp | CPU1 | ... | CPUx | systemTemp | fan1 | ... | fanY |
| ------ | ----- | ------ | ------ | ------ | ------ | ------ | ------ |
|2015-06-12 19:20:56 | 23 | ...| 29 | 21 | 14040 |	...	| na |
