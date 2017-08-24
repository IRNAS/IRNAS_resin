import time

import MAX1720x
import BQ2429x
import smbus as smbus


i2c_addr = 0x36

def main():
	'''
	#combined = i2c.read_word_data(i2c_addr, 0x09)
	combined = (i2c.read_byte_data(i2c_addr, 0x09 + 1) | (i2c.read_byte_data(i2c_addr, 0x09)))
	voltage = combined * 0.078125
	print "Reading all raw: " + str(voltage)
'''
	combined = i2c.read_word_data(i2c_addr, 0x09)
	print "Reading 16bit (raw): " + str(combined)
	print "raw hex: " + str(hex(combined))
	print combined * 0.078125

	#print "Reading with adatfruit driver:" + str(sensor_max.get_cell_voltage())
	#print "Reading with adatfruit current (signed): " + str(sensor_max.get_current())
	#debug_main()
	time.sleep(1)

def debug_main():
	print "-----------------------------------------------"
	print "MAX1720x : cell voltage : " + str(sensor_max.get_cell_voltage()) + "mV"
	print "MAX1720x : current : " + str(sensor_max.get_current())
	print "MAX1720x : temperature : " + str(sensor_max.get_temperature()) + "C"
	print "MAX1720x : SOC : " + str(sensor_max.get_SOC()) + "%"
	print ""
	'''print "BQ2429x : status - VSYS : " + str(sensor_bq.get_status(BQ2429x.VSYS_STAT))
	print "BQ2429x : status - THERM_STAT : " + str(sensor_bq.get_status(BQ2429x.THERM_STAT))
	print "BQ2429x : status - CHRG_STAT : " + str(sensor_bq.get_status(BQ2429x.CHRG_STAT))
	print "BQ2429x : fault - BAT_FAULT : " + str(sensor_bq.get_faults(BQ2429x.BAT_FAULT))
	print "BQ2429x : fault - CHRG_FAULT : " + str(sensor_bq.get_faults(BQ2429x.CHRG_FAULT))'''


def debug_it_all():

	print "-----------------------------------------------"
	print "MAX1720x : cell voltage : " + str(sensor_max.get_cell_voltage()) + "mV"
	print "MAX1720x : current : " + str(sensor_max.get_current())
	print "MAX1720x : temperature : " + str(sensor_max.get_temperature()) + "C"
	print "MAX1720x : SOC : " + str(sensor_max.get_SOC()) + "%"
	print "MAX1720x : capacity : " + str(sensor_max.get_capacity())
	print "MAX1720x : TTE : " + str(sensor_max.get_TTE())
	print "MAX1720x : TTF : " + str(sensor_max.get_TTF())
	print "MAX1720x : status : " + str(sensor_max.get_status())
	print "" 
	print ""
	print "BQ2429x : status - VSYS : " + str(sensor_bq.get_status(BQ2429x.VSYS_STAT))
	print "BQ2429x : status - THERM_STAT : " + str(sensor_bq.get_status(BQ2429x.THERM_STAT))
	print "BQ2429x : status - PG_STAT : " + str(sensor_bq.get_status(BQ2429x.PG_STAT))
	print "BQ2429x : status - DPM_STAT : " + str(sensor_bq.get_status(BQ2429x.DPM_STAT))
	print "BQ2429x : status - CHRG_STAT : " + str(sensor_bq.get_status(BQ2429x.CHRG_STAT))
	print "BQ2429x : status - VBUS_STAT : " + str(sensor_bq.get_status(BQ2429x.VBUS_STAT))
	print ""
	print "BQ2429x : fault - NTC_FAULT : " + str(sensor_bq.get_faults(BQ2429x.NTC_FAULT))
	print "BQ2429x : fault - BAT_FAULT : " + str(sensor_bq.get_faults(BQ2429x.BAT_FAULT))
	print "BQ2429x : fault - CHRG_FAULT : " + str(sensor_bq.get_faults(BQ2429x.CHRG_FAULT))
	print "BQ2429x : fault - BOOST_FAULT : " + str(sensor_bq.get_faults(BQ2429x.BOOST_FAULT))
	print "BQ2429x : fault - WATCHDOG_FAULT : " + str(sensor_bq.get_faults(BQ2429x.WATCHDOG_FAULT))
	print ""
	#print "BQ2429x : set charge voltage : " + str(sensor_bq.set_charge_voltage("110101", BQ2429x.PRECH_1, BQ2429x.THRESH_1))
	#print "BQ2429x : set ter_perch : " + str(sensor_bq.set_ter_prech_current(BQ2429x.TERM_CURRENT_DEFAULT,BQ2429x.PRECH_CURRENT_DEFAULT))


if __name__ == '__main__':

	sensor_max 	= MAX1720x.MAX1720x()
	sensor_bq	= BQ2429x.BQ2429x()

	i2c = smbus.SMBus(1)

	while 1:
		main()

