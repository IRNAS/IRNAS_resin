
'''
 * Name: bq2429x
 * Author: Silard Gal
 * Version: 1.0
 * Description: A library for interfacing the MAXIM MAX17201/MAX17205
 * 				Li+ fuel gauges.
 * Source: https://github.com/IRNAS/bq2429x
 * License: Copyright (c) 2017 Nick Lamprianidis 
 *          This library is licensed under the GPL license
 *          http://www.opensource.org/licenses/mit-license.php
 * Inspiration: The library is inspired by: https://github.com/IRNAS/bq2429x
 * Filename: bq2429x.py
 * File description: Definitions and methods for the bq2429x library
''' 

# bq2429x register addresses

BQ2429x_ADDR 						= 0x6b;
BQ2429x_INPUT_CTRL_ADDR 			= 0x00; # Input Source Control Register REG00 [reset = 00110xxx, or 3x]
BQ2429x_POWERON_CTRL_ADDR 			= 0x01; # Power-On Configuration Register REG01 [reset = 00011011, or 0x1B]
BQ2429x_CHARGE_CUR_CTRL_ADDR 		= 0x02; # Charge Current Control Register REG02 [reset = 01100000, or 60]
BQ2429x_PRECHARGE_CTRL_ADDR 		= 0x03; # Pre-Charge/Termination Current Control Register REG03 [reset = 00010001, or 0x11]
BQ2429x_CHARGE_VOL_CTRL_ADDR 		= 0x04; # Charge Voltage Control Register REG04 [reset = 10110010, or 0xB2]
BQ2429x_CHARGE_TERM_CTRL_ADDR 		= 0x05; # Charge Termination/Timer Control Register REG05 [reset = 10011010, or 0x9A]
BQ2429x_BOOST_THERMAL_CTRL_ADDR 	= 0x06; # Boost Voltage/Thermal Regulation Control Register REG06 [reset = 01110011, or 0x73]
BQ2429x_MISC_CTRL_ADDR 				= 0x07; # Misc Operation Control Register REG07 [reset = 01001011, or 4B]
BQ2429x_STATUS_ADDR 				= 0x08; # System Status Register REG08
BQ2429x_FAULT_ADDR 					= 0x09; # New Fault Register REG09
BQ2429x_VENDOR_ADDR 				= 0x0A; #/ Vender / Part / Revision Status Register REG0A

class BQ2429x(object):
	def __init__(self, address=BQ2429x_ADDR, i2c=None, **kwargs):
		if i2c is None:
			import Adafruit_GPIO.I2C as I2C
			i2c = I2C

		self._device = i2c.get_i2c_device(address, **kwargs)

	def get_status(self):
		#self._device.write8(BQ2429x_ADDR ,BQ2429x_STATUS_ADDR)
		return self._device.readU8(bq2429x_STATUS_ADDR)