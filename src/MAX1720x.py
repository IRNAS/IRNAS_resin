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
MAX1704X_ADDR 			= 0x36;
MAX1704X_VCELL_ADDR 	= 0x02;
MAX1704X_SOC_ADDR 		= 0x04;
MAX1704X_MODE_ADDR 		= 0x06;
MAX1704X_VERSION_ADDR 	= 0x08;
MAX1704X_CONFIG_ADDR 	= 0x0C;
MAX1704X_RCOMP_ADDR 	= 0x0C;
MAX1704X_ATHRD_ADDR 	= 0x0D;
MAX1704X_COMMAND_ADDR 	= 0xFE;

MAX17043				= 1
MAX17044				= 2

_IC 					= MAX17043

class MAX1720x(object):
	def __init__(self, address=MAX1720X_I2CADDR, i2c=None, **kwargs):
		if i2c is None:
			import Adafruit_GPIO.I2C as I2C
			i2c = I2C

		self._device = i2c.get_i2c_device(address, **kwargs)
	def get_voltage():
		self._device.writeRaw8(MAX1704X_VCELL_ADDR)
		return((self._device.readRaw8(MAX1704X_VCELL_ADDR) << 4) + (self._device.readRaw8(MAX1704X_VCELL_ADDR) >> 4)) * 0.00125 * _IC
