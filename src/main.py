import time

import BMP280
import MAX1720x

def main():
	sensor = MAX1720x.MAX1720x()

	temp =  sensor.get_temperature()
	print "Returned: " + str(temp)
	print "/256: " + str(temp/256)
	combined = temp | (temp << 8)
	print "combined: " + str(combined)
	print "combined/256: " + str(combined/256)

	time.sleep(1)

if __name__ == '__main__':
	while 1:
		main()

