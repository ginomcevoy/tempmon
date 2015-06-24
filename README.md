# tempmon
Distributed Temperature Monitor using IPMI

## Requirements:
- ipmi-tools on the head server
- Python 2.6+ on the head server
- The head server must be able to reach the nodes via an IPMI address

## Usage:
- ./tempmon-start.sh to start monitoring the nodes
- ./tempmon-stop.sh to stop monitoring the nodes
- ./tempmon-status.sh query the state of Tempmon

## Configuration:
- ``hosts`` file: list the hostnames or IP addresses of the nodes to monitor. If using hostnames, these should be resolved via the ``/etc/hosts`` file.
- ``config`` file: Holds Tempmon parameters. Main parameters:
  - ``SENSOR_INTERVAL``: frequency of monitoring, in seconds (default: 3600 seconds / 1 hour)
  - ``OUTPUT_DIR``: directory that will hold output data (default: ``$HOME/ipmi-data``)
  - ``HOST_FILE``: indicates host file to read (default: ``hosts``)