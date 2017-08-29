import time

import MAX1720x
import BQ2429x
import smbus as smbus

def main():
	debug_main()
	time.sleep(6)

def debug_main():

	print "-----------------------------------------------"
	print "MAX1720x : cell voltage    	 : " + str(sensor_max.get_cell_voltage()) + "mV"
	print "MAX1720x : max voltage     	 : " + str(sensor_max.get_max_voltage()) + "mV"
	print "MAX1720x : current         	 : " + str(sensor_max.get_current()) + "mA"
	print "MAX1720x : avg_current     	 : " + str(sensor_max.get_avg_current()) + "mA"
	print "MAX1720x : max&min_current 	 : " + str(sensor_max.get_maxmin_current())
	print "MAX1720x : temperature 	  	 : " + str(sensor_max.get_temperature()) + "C"
	print "MAX1720x : SOC             	 : " + str(sensor_max.get_SOC()) + "%"
	print "MAX1720x : Battery         	 : " + str(sensor_max.get_battery_absent())
	print ""
	print "BQ2429x : status - VSYS       : " + str(sensor_bq.get_status(BQ2429x.VSYS_STAT))
	print "BQ2429x : status - THERM_STAT : " + str(sensor_bq.get_status(BQ2429x.THERM_STAT))
	print "BQ2429x : status - CHRG_STAT  : " + str(sensor_bq.get_status(BQ2429x.CHRG_STAT))
	print "BQ2429x : fault - BAT_FAULT   : " + str(sensor_bq.get_faults(BQ2429x.BAT_FAULT))
	print "BQ2429x : fault - CHRG_FAULT  : " + str(sensor_bq.get_faults(BQ2429x.CHRG_FAULT))

def debug_it_all():

	print "========================================================"
	print "MAX1720x : cell voltage -------- : " + str(sensor_max.get_cell_voltage()) + "mV"
	print "MAX1720x : max voltage --------- : " + str(sensor_max.get_maxmin_voltage()) + "mV"
	print "MAX1720x : current ------------- : " + str(sensor_max.get_current())
	print "MAX1720x : avg_current --------- : " + str(sensor_max.get_avg_current()) + "mA"
	print "MAX1720x : max&min_current ----- : " + str(sensor_max.get_max_current())
	print "MAX1720x : temperature --------- : " + str(sensor_max.get_temperature()) + "C"
	print "MAX1720x : SOC ----------------- : " + str(sensor_max.get_SOC()) + "%"
	print "MAX1720x : capacity ------------ : " + str(sensor_max.get_capacity())
	print "MAX1720x : TTE ----------------- : " + str(sensor_max.get_TTE())
	print "MAX1720x : TTF ----------------- : " + str(sensor_max.get_TTF())
	print "MAX1720x : Battery ------------- : " + str(sensor_max.get_battery_absent())
	print "" 
	print "BQ2429x : status - VSYS --------- : " + str(sensor_bq.get_status(BQ2429x.VSYS_STAT))
	print "BQ2429x : status - THERM_STAT --- : " + str(sensor_bq.get_status(BQ2429x.THERM_STAT))
	print "BQ2429x : status - PG_STAT ------ : " + str(sensor_bq.get_status(BQ2429x.PG_STAT))
	print "BQ2429x : status - DPM_STAT ----- : " + str(sensor_bq.get_status(BQ2429x.DPM_STAT))
	print "BQ2429x : status - CHRG_STAT ---- : " + str(sensor_bq.get_status(BQ2429x.CHRG_STAT))
	print "BQ2429x : status - VBUS_STAT ---- : " + str(sensor_bq.get_status(BQ2429x.VBUS_STAT))
	print ""
	print "BQ2429x : fault - NTC_FAULT ----- : " + str(sensor_bq.get_faults(BQ2429x.NTC_FAULT))
	print "BQ2429x : fault - BAT_FAULT ----- : " + str(sensor_bq.get_faults(BQ2429x.BAT_FAULT))
	print "BQ2429x : fault - CHRG_FAULT ---- : " + str(sensor_bq.get_faults(BQ2429x.CHRG_FAULT))
	print "BQ2429x : fault - BOOST_FAULT --- : " + str(sensor_bq.get_faults(BQ2429x.BOOST_FAULT))
	print "BQ2429x : fault - WATCHDOG_FAULT  : " + str(sensor_bq.get_faults(BQ2429x.WATCHDOG_FAULT))
	print ""

if __name__ == '__main__':

	# referencing the sensors
	sensor_max 	= MAX1720x.MAX1720x()
	sensor_bq	= BQ2429x.BQ2429x()

	# reset the minmax
	sensor_max.reset_minmax_current()
	
	# set the update of the average current 5s
	sensor_max.set_average_current_update_time(4)

	while 1:
		main()

