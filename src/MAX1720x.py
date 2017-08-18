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

# MAX1720X register addresses
MAX1720X_STATUS_ADDR 	= 0x00; # Contains alert status and chip status
MAX1720X_VCELL_ADDR 	= 0x09; # Lowest cell voltage of a pack, or the cell voltage for a single cell
MAX1720X_REPSOC_ADDR 	= 0x06; # Reported state of charge
MAX1720X_REPCAP_ADDR 	= 0x05; # Reported remaining capacity
MAX1720X_TEMP_ADDR 		= 0x08; # Temperature
MAX1720X_CURENT_ADDR 	= 0x0A; # Battery current
MAX1720X_TTE_ADDR 		= 0x11; # Time to empty
MAX1720X_TTF_ADDR 		= 0x20; # Time to full
MAX1720X_CAPACITY_ADDR 	= 0x10; # Full capacity estimation
MAX1720X_VBAT_ADDR 		= 0xDA; # Battery pack voltage
MAX1720X_AVCELL_ADDR 	= 0x17; # Battery cycles
MAX1720X_COMMAND_ADDR 	= 0x60; # Command register
MAX1720X_CONFIG2_ADDR 	= 0xbb; # Command register

class MAX1720x(object):
	def __init__(self, address=MAX1720X_I2CADDR, i2c=None, **kwargs):
		if i2c is None:
			import Adafruit_GPIO.I2C as I2C
			i2c = I2C

		self._device = i2c.get_i2c_device(address, **kwargs)

	def get_voltage(self):
		data = (self._device.readU8(MAX1720X_VCELL_ADDR)) | (self._device.readU8(MAX1720X_VCELL_ADDR) << 8) 
		return data*0.078125; 

	def get_temperature(self):
		data = self._device.readS16(MAX1720X_TEMP_ADDR) 
		return data/256; 