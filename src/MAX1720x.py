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
import Adafruit_GPIO.I2C as I2C
i2c = I2C

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

class MAX1720x(object):
	def __init__(self):
		try:
			self._device = i2c.get_i2c_device(MAX1720X_I2CADDR)
		except:
			print "Couldn't connect to MAX1720 | I2C init"

	# def get_cell_voltage(self) - gets a cell voltage (~3V)
	def get_cell_voltage(self):
		try:
			combined = self._device.readU16(MAX1704X_VCELL_ADDR)
			value = combined * 0.078125
			return value	

		except:
			print "Couldn't connect to MAX1720"
			return 0

	
