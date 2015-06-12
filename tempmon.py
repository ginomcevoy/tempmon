'''
Created on Jun 11, 2015

Routines for parsing and saving sensor data.

@author: Giacomo Mc Evoy - giacomo@lncc.br
'''

import csv
import io
import os
import re
import sys

def parseSensorData(inputFile, timeStamp):
	'''
	Parses data from a single IPMI sensor call.
	:param inputFile: file containing IPMI sensor data
	:param timeStamp 
	:returns: SensorItem instance
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
					if splits[1].strip() == 'na':
						fanSpeed = 'na'
					else:
						fanSpeed = -1

				fanSpeeds.append(fanSpeed)

	return SensorItem(timeStamp, cpuTemps, systemTemp, fanSpeeds)

def appendSensorData(sensorItem, outputFilename):
	'''
	Adds a tuple to a CSV file. Creates the file if it does not exist.
	:param sensorItem: populated SensorItem instance 
	:param outputFilename: string with full path of the output file.
	'''
	csvFile = None
	csvWriter = None
	if os.path.isfile(outputFilename):
		csvFile = open(outputFilename, 'a')
		csvWriter = csv.writer(csvFile, delimiter=',',
	                      lineterminator='\n', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		
	else:
		if os.path.isdir(outputFilename):
			# path is a dir...
			raise ValueError('Path cannot be a dir: ' + outputFilename)

		# file does not exist, create it with a header
		csvFile = open(outputFilename, 'w')
		csvWriter = csv.writer(csvFile, delimiter=',',
	                        lineterminator='\n', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		header = __createHeader__(sensorItem)
		csvWriter.writerow(header)

	# file now exists with at least a header, update content with a new tuple
	__addSensorTuple__(sensorItem, csvWriter)
	csvFile.close()	
	
def __createHeader__(sensorItem):
	'''
	Creates the header list using provided metadata, example:
	[timeStamp,cpu1,cpu2,systemTemp,fan1,fan2,fan3,fan4]
	:param sensorItem: populated SensorItem instance, for metadata 
	'''
	header = ['timeStamp']

	# add CPU temperatures
	for i in range(1, len(sensorItem.cpuTemps)+1):
		cpuHeader = 'CPU'+str(i)
		header.append(cpuHeader)

	# add systemTemp
	header.append('systemTemp')

	# add fan speeds
	for i in range(1, len(sensorItem.fanSpeeds)+1):
		fanHeader = 'fan'+str(i)
		header.append(fanHeader)

	return header


def __addSensorTuple__(sensorItem, csvWriter):
	'''
	Adds the tuple to a CSV file. The file must exist and have a header.
	:param sensorItem: populated SensorItem instance to add
	:param csvWriter: object that can write to open CSV file
	:returns the csvWriter
	'''
	aTuple = [sensorItem.timeStamp]

	# add CPU temperatures
	for i in range(0, len(sensorItem.cpuTemps)):
		aTuple.append(str(sensorItem.cpuTemps[i]))

	# add systemTemp
	aTuple.append(str(sensorItem.systemTemp))

	# add fan speeds
	for i in range(0, len(sensorItem.fanSpeeds)):
		aTuple.append(str(sensorItem.fanSpeeds[i]))

	# add tuple to CSV
	csvWriter.writerow(aTuple)
	return csvWriter

class SensorItem:

	'''
	Stores relevant data from a single IPMI sensor call, as well as the timeStamp
	of the call
	:param timeStamp: value for date and time of the measurement
	:param cpuTemps: list of CPU temperatures
	:param systemTemp: value of System temperature
	:param fans: list of fan speeds
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

if __name__ == '__main__':

    # verify input
    if len(sys.argv) < 4:
    	print("call: tempmon <inputFile> <timeStamp> <outputFile>")
    	exit(1)

    # parse arguments and call routine
    inputFile = sys.argv[1]
    timeStamp = sys.argv[2]
    outputFile = sys.argv[3]

    sensorItem = parseSensorData(inputFile, timeStamp)
    appendSensorData(sensorItem, outputFile)
