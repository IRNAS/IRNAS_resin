import time

import BMP280
import MAX1720x
import BQ2429x

def main():
	'''
	print "-----------------------------------------------"
	print "MAX1720x : cell voltage : " + str(sensor_max.get_cell_voltage()) + "mV"
	print "MAX1720x : current : " + str(sensor_max.get_current())
	print "MAX1720x : temperature : " + str(sensor_max.get_temperature()) + "C"
	print "MAX1720x : SOC : " + str(sensor_max.get_SOC()) + "%"
	print "MAX1720x : capacity : " + str(sensor_max.get_capacity())
	print "MAX1720x : TTE : " + str(sensor_max.get_TTE())
	print "MAX1720x : TTF : " + str(sensor_max.get_TTF())
	print "MAX1720x : status : " + str(sensor_max.get_status())
	print "BQ2429x : faults : " + str(sensor_bq.get_faults())'''

	'''print "-----------------------------------------------"
	print "BQ2429x : status - VSYS : " + str(sensor_bq.get_status(BQ2429x.VSYS_STAT))
	print "BQ2429x : status - THERM_STAT : " + str(sensor_bq.get_status(BQ2429x.THERM_STAT))
	print "BQ2429x : status - PG_STAT : " + str(sensor_bq.get_status(BQ2429x.PG_STAT))
	print "BQ2429x : status - DPM_STAT : " + str(sensor_bq.get_status(BQ2429x.DPM_STAT))
	print "BQ2429x : status - CHRG_STAT : " + str(sensor_bq.get_status(BQ2429x.CHRG_STAT))
	print "BQ2429x : status - VBUS_STAT : " + str(sensor_bq.get_status(BQ2429x.VBUS_STAT))

	print "BQ2429x : fault - NTC_FAULT : " + str(sensor_bq.get_faults(BQ2429x.NTC_FAULT))
	print "BQ2429x : fault - BAT_FAULT : " + str(sensor_bq.get_faults(BQ2429x.BAT_FAULT))
	print "BQ2429x : fault - CHRG_FAULT : " + str(sensor_bq.get_faults(BQ2429x.CHRG_FAULT))
	print "BQ2429x : fault - BOOST_FAULT : " + str(sensor_bq.get_faults(BQ2429x.BOOST_FAULT))
	print "BQ2429x : fault - WATCHDOG_FAULT : " + str(sensor_bq.get_faults(BQ2429x.WATCHDOG_FAULT))'''

	time.sleep(1)

if __name__ == '__main__':

	sensor_max 	= MAX1720x.MAX1720x()
	sensor_bq	= BQ2429x.BQ2429x()

	while 1:
		main()

