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
	print "MAX1720x : status : " + str(sensor_max.get_status())'''

	print sensor_bq.get_status()
	print sensor_bq.get_faults()
	print sensor_bq.set_charge_voltage()
	time.sleep(1)

if __name__ == '__main__':

	sensor_max 	= MAX1720x.MAX1720x()
	sensor_bq	= BQ2429x.BQ2429x()

	while 1:
		main()

