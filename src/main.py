import time

import BMP280
import MAX1720x
import BQ2429x

def main():

	print "MAX1720x : cell voltage : " + sensor_max.get_cell_voltage()

	time.sleep(1)

if __name__ == '__main__':

	sensor_max = MAX1720x.MAX1720x()

	while 1:
		main()

