import time

import BMP280
import MAX1720x
import BQ2429x

def main():
	#sensor = BQ2429x.BQ2429x()
	#print sensor.get_status()
	sensor = MAX1720x.MAX1720x()
	print "MAX1720 : cell voltage : " + str(sensor.get_cell_voltage())
	#rint "MAX1720 : current : " + str(sensor.get_current()) 
	#print "MAX1720 : temp : " + str(sensor.get_temperature())

	time.sleep(5)

if __name__ == '__main__':


	while 1:
		main()

