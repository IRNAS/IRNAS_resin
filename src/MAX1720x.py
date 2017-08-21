'''
 * Name: MAX1720x
 * Author: Silard Gal
 * Version: 1.0
 * Description: A library for interfacing the MAXIM MAX17201/MAX17205
 * 				Li+ fuel gauges.
 * Source: https://github.com/IRNAS/max1720x/
 * License: Copyright (c) 2017 Nick Lamprianidis 
 *          This library is licensed under the GPL license
 *          http://www.opensource.org/licenses/mit-license.php
 * Inspiration: The library is inspired by: https://github.com/IRNAS/max1720x/
 * Filename: max1720x.py
 * File description: Definitions and methods for the max1720x library
'''

import logging
import time

MAX1720X_I2CADDR = 0x36

# MAX1704X register addresses
MAX1704X_STATUS_ADDR 	= 0x00; # Contains alert status and chip status
MAX1704X_VCELL_ADDR 	= 0x09; # Lowest cell voltage of a pack, or the cell voltage for a single cell
MAX1704X_REPSOC_ADDR 	= 0x06; # Reported state of charge
MAX1704X_REPCAP_ADDR 	= 0x05; # Reported remaining capacity
MAX1704X_TEMP_ADDR 		= 0x08; # Temperature
MAX1704X_CURENT_ADDR 	= 0x0A; # Battery current
MAX1704X_TTE_ADDR 		= 0x11; # Time to empty
MAX1704X_TTF_ADDR 		= 0x20; # Time to full
MAX1704X_CAPACITY_ADDR 	= 0x10; # Full capacity estimation
MAX1704X_VBAT_ADDR 		= 0xDA; # Battery pack voltage
MAX1704X_AVCELL_ADDR 	= 0x17; # Battery cycles
MAX1704X_COMMAND_ADDR 	= 0x60; # Command register
MAX1704X_CONFIG2_ADDR 	= 0xbb; # Command register

MAX17043				= 1
MAX17044				= 2

_IC 					= MAX17044

class MAX1720x(object):
	def __init__(self, address=MAX1720X_I2CADDR, i2c=None, **kwargs):
		if i2c is None:
			import Adafruit_GPIO.I2C as I2C
			i2c = I2C

		try:
			self._device = i2c.get_i2c_device(address, **kwargs)
		except:
			print "Couldn't connect to MAX1720"

	# def get_cell_voltage(self) - gets a cell voltage (~3V)
	def get_cell_voltage(self):
		#self._device.writeRaw8(MAX1704X_VCELL_ADDR) 	# no need for this really, but we will keep it
		try:
			return((self._device.readU8(MAX1704X_VCELL_ADDR) << 4) + (self._device.readU8(MAX1704X_VCELL_ADDR) >> 4)) * 0.00125 * _IC
		except:
			print "Couldn't connect to MAX1720"
			return 0
	# def get_SOC(self) - returns the relative state of charge of the connected LiIon Polymer battery (as a percentage of the full capacity w/ resolution 1/256%)
	def get_SOC(self):
		try:
			return(self._device.readU8(MAX1704X_REPSOC_ADDR) + self._device.readU8(MAX1704X_REPSOC_ADDR) / 256)
		except:
			print "Couldn't connect to MAX1720"
			return 0
	'''def get_current(self):
		return((self._device.readU8(MAX1704X_CURENT_ADDR) << 4) + (self._device.readU8(MAX1704X_CURENT_ADDR) >> 4)) *0.0015625/0.01 

	def get_temperature(self):
		return( (self._device.readU8(MAX1704X_TEMP_ADDR) << 4) + (self._device.readU8(MAX1704X_TEMP_ADDR) >> 4) ) / 256
'''