import time

import BMP280

def main():
	sensor = BMP280.BMP280()
	print "Temperature: " 	+ sensor.read_temperature()
	print "Pressure: " 		+ sensor.read_pressure()
	time.sleep(1)

if __name__ == '__main__':
	while 1:
		main()

