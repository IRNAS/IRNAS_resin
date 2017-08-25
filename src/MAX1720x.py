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
import smbus as smbus
import Adafruit_GPIO.I2C as I2C
#i2c = I2C

MAX1720X_I2CADDR = 0x36

# MAX1704X register addresses
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
	def __init__(self):
		try:
			self._device = I2C.get_i2c_device(MAX1720X_I2CADDR)					# connect to device
			self.i2c = smbus.SMBus(1)
		except:
			print "Couldn't connect to MAX1720 | I2C init"						# coudlnt connect to i2c unit

	# def get_cell_voltage(self, number) - get the voltage on a specific voltage
	def get_cell_voltage(self):
		try:						
			value 	= self.i2c.read_word_data(MAX1720X_I2CADDR, MAX1720X_VCELL_ADDR)	# get the value dependents on the cell nu,ber
			return float(value) * 0.078125												# to get actual voltage need to calculate
		except:
			print "Couldn't connect to MAX1720"
			return 0

	# def get_current(self) - gets the current with calculation of 0.0015625 mV/Ohm
	def get_current(self):
		try:
			combined 	= self._device.readS16(MAX1720X_CURENT_ADDR)			# read the current register
			return float((combined * 0.0015625) / 0.010)
		except:
			print "Couldn't connect to MAX1720"
			return 0

	def get_avg_current(self):
		try:
			combined 	= self._device.readS16(0x0B)
			return float((combined * 0.0015625) / 0.010)
		except:
			print "Couldn't connect to MAX1720"
			return 0

	def get_max_current(self):
		try:
			'''combined = self._device.readU16(0x1C)
			print "hex: " + str(bin(combined))
			hi = ((combined >> 8) & 0xff)
			lo = ((combined >> 0) & 0xff)
			return "hi: " + str(hi) + " lo: " + str(lo)'''
			current_enable = self._device.readU16(0x1BA)
			new_enable = current_enable | 0b0000000000010000
			print hex(new_enable)
			#print "writing: " + str(self._device.write16(0x1BA, hex(new_enable)))
			#self._device.write16(0x1BA, hex(new_enable))
			self.i2c.write_word_data(0x37, 0x1BA, hex(new_enable))
			return hex(self._device.readU16(0x1BA))
		except:
			print "Couldn't connect to MAX1720"
			return 0

	# def get_temperature(self) - getting the chip (surroundings) temperature
	def get_temperature(self):
		try:
			combined 	= self._device.readU16(MAX1720X_TEMP_ADDR)				# read the temp register
			value 		= combined / 256.0										# divide by 256 to get real value
			return float(value)													# return value but float
		except:
			print "Couldn't connect to MAX1720"
			return 0

	# def get_SOC(self) - the relative state of charge of the connected LiIon Polymer battery as a percentage of the full capacity w/ resolution 1/256%
	def get_SOC(self):
		try:
			combined 	= self._device.readU16(MAX1720X_REPSOC_ADDR)			# read the soc register
			value 		= combined / 256										# divide by 256 to get real value
			return value														# return value
		except:
			print "Couldn't connect to MAX1720"
			return 0

	# def get_capacity(self) - RepCap or reported capacity is a filtered version of the AvCap register that prevents large jumps in the reported value caused by changes in the application such as abrupt changes in temperature or load current.
	def get_capacity(self):
		try:
			combined 	= self._device.readU16(MAX1720X_REPCAP_ADDR)			# read the capacity register
			value 		= combined * 0.005 / 0.01								# get the real value
			return value														# return the value
		except:
			print "Couldn't connect to MAX1720"
			return 0

	# def get_TTE(self) - the TTE register holds the estimated time to empty for the application under present temperature and load conditions 
	def get_TTE(self):
		try:
			combined  	= self._device.readU16(MAX1720X_TTE_ADDR)				# read the tte register
			value 		= combined * 5.625 										# we are calculating actual value with 5.625s
			return value 														# return the value
		except:
			print "Couldn't connect to MAX1720"
			return 0

	# def get_TTF(self) - the TTF register holds the estimated time to full for the application under present conditions. 
	def get_TTF(self):
		try:
			combined 	= self._device.readU16(MAX1720X_TTF_ADDR)				# read the ttf register
			value 		= combined * 5.625										# we are calculating actual value with 5.625s
			return value														# return the value
		except:
			print "Couldn't connect to MAX1720"
			return 0
			
	# def get_status(self) - Status Register (000h) The Status register maintains all flags related to alert thresholds and battery insertion or removal.	
	def get_status(self):
		try:
			value 		= self._device.readU16(MAX1720X_STATUS_ADDR)			# read the status register
			return value														# return the value
		except:
			print "Couldn't connect to MAX1720"
			return 0
