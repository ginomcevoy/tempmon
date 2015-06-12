'''
Created on Jun 11, 2015

Unit tests for the tempmon module.

@author: Giacomo Mc Evoy - giacomo@lncc.br
'''

import os
import shutil

import tempmon
from tempmon import SensorItem

import unittest

class TempmonTest(unittest.TestCase):
	'''
	Unit tests for tempmon.parseSensorData
	'''

	def setUp(self):
		self.timeStamp = 'aTimeStamp'
		self.expected = SensorItem(self.timeStamp, [29.0,28.0], 23.0, [14040.0, 14040.0, 14040.0, 'na'])
		self.inputFile = 'test/example.in'

	def testParseSensorData(self):
		sensorItem = tempmon.parseSensorData(self.inputFile, self.timeStamp)
		self.maxDiff = None
		self.assertEqual(sensorItem.__dict__, self.expected.__dict__)

class AppendSensorData(unittest.TestCase):
	'''
	Unit tests for tempmon.appendSensorData
	'''

	def setUp(self):
		self.sensorItem = SensorItem('1999-01-08 04:05:06', [29.0,28.0], 23.0, [14040.0, 14040.0, 14040.0, 'na'])

		# for testing empty CSV
		self.emptyOutputFilename = '/tmp/tempmon-appendTest-empty.csv'
		self.expectedOutputForEmpty = 'test/append-empty.csv'

		# for testing existing CSV
		self.existingInputFile = 'test/append-existing-input.csv'
		self.existingOutputFilename = '/tmp/tempmon-appendTest-existing.csv'
		self.expectedExistingOutput = 'test/append-existing-output.csv'

	def testAppendSensorDataEmpty(self):
		# Start from an empty file, expect a file with a header and a single tuple

		# make sure the output does not exist
		if os.path.isfile(self.emptyOutputFilename):
			os.remove(self.emptyOutputFilename)

		# generate the output
		tempmon.appendSensorData(self.sensorItem, self.emptyOutputFilename)

		# verify output
		self.maxDiff = None
		actualContent = open(self.emptyOutputFilename, 'r').read()
		expectedContent = open(self.expectedOutputForEmpty, 'r').read()
		self.assertEqual(actualContent, expectedContent)

	def testAppendSensorDataExisting(self):
		# Start from a populated file, expect a file with some tuples. 
		# Last tuple must be added tuple

		# copy existing output (input to routine) for idempotence of test
		shutil.copyfile(self.existingInputFile, self.existingOutputFilename)

		# use existing outputFile to append output
		tempmon.appendSensorData(self.sensorItem, self.existingOutputFilename)

		# verify output
		self.maxDiff = None
		actualContent = open(self.existingOutputFilename, 'r').read()
		expectedContent = open(self.expectedExistingOutput, 'r').read()
		self.assertEqual(actualContent, expectedContent)

if __name__ == '__main__':
    unittest.main()