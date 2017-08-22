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
	#sensor_bq.set_charge_voltage(0)
	#sensor_bq.set_charge_current(0)
	#sensor_bq.set_input_current_limit(0)
	#sensor_max.get_cell_voltage(1)

	print "BQ2429x : status : " + str(sensor_bq.get_status(BQ2429x.VSYS_STAT))




	time.sleep(1)

if __name__ == '__main__':

	sensor_max 	= MAX1720x.MAX1720x()
	sensor_bq	= BQ2429x.BQ2429x()

	while 1:
		main()

