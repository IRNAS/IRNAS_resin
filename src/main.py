import time

import BMP280
import MAX1720x

def main():
	sensor = MAX1720x.MAX1720x()

	temp =  sensor.get_temperature()
	print "Returned: " + str(temp)

	time.sleep(1)

if __name__ == '__main__':
	while 1:
		main()

