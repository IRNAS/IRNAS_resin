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

# -*- coding: UTF-8 -*-

import logging
import time
import smbus as smbus
import Adafruit_GPIO.I2C as I2C

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
			self._device = I2C.get_i2c_device(MAX1720X_I2CADDR)							# connect to device
			self.i2c = smbus.SMBus(1)													# low level i2c bus

			current_enable = self._device.readU16(0x1BA)								# current enable
			new_enable = current_enable | 0b0000000000010000							# enable minmax current
			self.i2c.write_word_data(0x36, 0x1BA, new_enable)							# write it

			# check if it is really enabled
			if new_enable != self._device.readU16(0x1BA):
				print "It is not the same register"
				return 0

			#self.i2c.write_word_data(0x36, 0x1CF,0x03E8)								# set the rsense register to 0.010ohm

		except:
			print "Couldn't connect to MAX1720 | I2C init"								# coudlnt connect to i2c unit

	# def get_cell_voltage(self, number) - get the voltage on a specific voltage
	def get_cell_voltage(self):
		'''try:						
			value 	= self.i2c.read_word_data(MAX1720X_I2CADDR, MAX1720X_VCELL_ADDR)	# get the value dependents on the cell nu,ber
			return str(float(value) * 0.078125)  + "mV"									# to get actual voltage need to calculate
		except:
			return "Couldn't connect to MAX1720 <----"'''
		return "Couldn't connect to MAX1720 <---- !!!!!"

	# def get_current(self) - gets the current with calculation of 0.0015625 mV/Ohm
	def get_current(self):
		try:
			combined 	= self._device.readS16(MAX1720X_CURENT_ADDR)					# read the current register
			return float((combined * 0.0015625) / 0.010)								# calculate it with 0.0015625 mV/Ohm
		except:
			print "Couldn't connect to MAX1720"
			return 0

	# def get_avg_current(self) - gets the average current
	def get_avg_current(self):
		try:
			combined 	= self._device.readS16(0x0B)									# read the register			
			return float((combined * 0.0015625) / 0.010)								# calculate it with 0.0015625 mV/Ohm
		except:
			print "Couldn't connect to MAX1720"
			return 0

	# def get_maxmin_voltage(self) - gets the max voltage in mV
	def get_max_voltage(self):

		# 20mV resolution -> register * 20mV -> register * 0.02
		# to get mV we just do -> register * 0.02 * 1000 
		# the * 1000 is to getting from V to mV

		try:
			combined = self._device.readU16(0x01B)								# read register minmax voltage	
			maximum = (combined >> 8) & 0xFF 									# get the maximum 
			minimum = (combined >> 0) & 0xFF 									# get the minimum

			# debugging
			'''print "Combined" + str(combined) + " " + str(bin(combined))
			print "Maximum" + str(maximum) + " " + str(bin(maximum))
			print "Minimum" + str(minimum) + " " + str(bin(minimum))'''

			# getting the real mV value
			float_maximum = float(maximum * 0.02 * 1000)						# calculating by the formula above

			return float_maximum												# return it
			
		except:
			print "Couldn't connect to MAX1720"
			return 0

	def get_maxmin_current(self):

		# .0004mV / Rsense resolution
		# 0.0004V / 0.010ohm resolution
		# 0.04 resolution
		# that is 40mA resolution!

		try:
			combined 		= self._device.readS16(0x01C)						# reading the reg
			maximum 		= (combined >> 8) & 0xFF							# getting max
			minimum 		= (combined >> 0) & 0xFF 							# getting min

			# debugging
			'''
			print "Combined" + str(combined) + " " + str(bin(combined))
			print "Maximum" + str(maximum) + " " + str(bin(maximum))
			print "Minimum" + str(minimum) + " " + str(bin(minimum))
			'''

			# calculating based on the top formula
			float_maximum = float(maximum * 0.04 * 1000)						# calculate max
			float_minimum = float(-(10200 - (minimum * 0.04 * 1000)))			# calculate min

			# checking if it is a valid value
			if maximum == 255 or maximum == 128:
				float_maximum = "invalid"
			else:
				float_maximum = str(float_maximum) + "mA"

			if minimum == 255 or minimum == 0:
				float_minimum = "invalid"
			else:
				float_minimum = str(float_minimum) + "mA"

			if maximum == 128 and (minimum == 127 or minimum == 255):
				float_maximum = "invalid"
				float_minimum = "invalid"

			# returning it 
			return "Max: " + str(float_maximum)+ "   " + "Min: " + str(float_minimum)

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
			
	# def get_battery_absent(self) - checks if the battery is present
	def get_battery_absent(self):

		# d3 -> 3rd bit -> checks if battery is here
		# returns 0 if yes and 1 if not present

		try:
			value 		= self._device.readU16(MAX1720X_STATUS_ADDR)			# read the status register
			#print bin(value)													# debug	
			if (value >> 3) & 1:												# checks that bit
				return "Battery not present"
			else:
				return "Battery present"
		except:
			print "Couldn't connect to MAX1720"
			return 0

	# def reset_minmax_current(self) - reset the minmax register t defaul 0x807F
	def reset_minmax_current(self):
		try:
			self.i2c.write_word_data(0x36, 0x01C, 0x807F)						# reset the minmax 
		except:
			print "Couldn't reset minmax current"
			return 0

	# def set_average_update_time(self, value) - set the average update of the average current register 
	def set_average_current_update_time(self, value):

		# the formula is calculated by 45 * 2^(value-7) = x seconds

		# table of seconds
		# 0 -> 0,35s    3 -> 2,8s    6 -> 22,5s  9  -> 3min   12 -> 24min   15 -> 3,2h
		# 1 -> 0,703s   4 -> 5,65s   7 -> 45s    10 -> 6min   13 -> 48min
		# 2 -> 1,40     5 -> 11,12s  8 -> 90s    11 -> 12min  14 -> 1,6h

		try:
			current_reg =  self._device.readU16(0x029)
			current_reg = current_reg & 0xFFF0									# with this we are clearing the 4 bits we want to set after
			
			# with (value & 0x000F) we make it copy the good values but set everything else to 0
			# with current_reg | (value & 0x000F) we make it "copy" the other values from the current reg to the value
			new_reg_value = current_reg | (value & 0x000F)	

			# checking register 
			self.i2c.write_word_data(0x36, 0x029, new_reg_value)
			if self._device.readU16(0x029) == new_reg_value:
				print "All good"
			else:
				print "something went wrong"

		except:
			print "Couldn't reset minmax current"
			return 0