'''
Created on Jun 11, 2015

@author: Giacomo Mc Evoy - giacomo@lncc.br
'''

import tempmon
from tempmon import SensorItem

import unittest

class GetHardwareInfoTest (unittest.TestCase):

	def setUp(self):
		self.timeStamp = 'aTimeStamp'
		self.expected = SensorItem(self.timeStamp, [29.0,28.0], 23.0, [14040.0, 14040.0, 14040.0, -1])
		self.inputFile = 'test/example.in'

	def testParse(self):
		sensorItem = tempmon.parseSensorData(self.inputFile, self.timeStamp)
		self.maxDiff = None
		self.assertEqual(sensorItem.__dict__, self.expected.__dict__)


if __name__ == '__main__':
    unittest.main()