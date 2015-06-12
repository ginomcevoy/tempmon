'''
Created on Jun 11, 2015

@author: Giacomo Mc Evoy - giacomo@lncc.br
'''

import re

def parseSensorData(inputFile, timeStamp):
	'''
	Reads data from a single IPMI sensor call, parses it and generates a
	SensorItem instance.
	@param inputFile: file containing IPMI sensor data
	'''
	cpuTemps=[]
	systemTemp=-1
	fanSpeeds=[]

	# Read whole text
	with open(inputFile, 'r') as sensorFile:
		sensorText = sensorFile.read()

		# Work each line
		lines = sensorText.split('\n')
		for line in lines:

			if re.match('CPU[0-9]\sTemp*', line):
				# line for CPU temperature
				splits = line.split('|')
				try:
					cpuTemp = float(splits[1])
				except (ValueError):
					# CPU temp could not be read
					cpuTemp = -1

				cpuTemps.append(cpuTemp)
				
			if re.match('System.Temp*', line):
				# line for System temperature
				splits = line.split('|')
				try:
					systemTemp = float(splits[1])
				except (ValueError):
					# system temp could not be read
					systemTemp = -1

			if re.match('Fan[0-9]*', line):
				# line for fan speed
				splits = line.split('|')
				try:
					fanSpeed = float(splits[1])
				except (ValueError):
					# fan speed could not be read
					fanSpeed = -1

				fanSpeeds.append(fanSpeed)

	return SensorItem(timeStamp, cpuTemps, systemTemp, fanSpeeds)

class SensorItem:

	'''
	Stores relevant data from a single IPMI sensor call, as well as the timeStamp
	of the call
	@param timeStamp: indicates the date and time of the measurement
	@param cpuTemps: list of CPU temperatures
	@param systemTemp: value of System temperature
	@param fans: list of fan speeds
	'''
	def __init__(self, timeStamp, cpuTemps, systemTemp, fanSpeeds):
		self.timeStamp = timeStamp
		self.cpuTemps = cpuTemps
		self.systemTemp = systemTemp
		self.fanSpeeds = fanSpeeds

	def __str__(self):
		return str(self.__dict__)

	def __eq__(self, other): 
		return self.__dict__ == other.__dict__