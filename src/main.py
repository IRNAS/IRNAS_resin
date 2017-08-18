import time

import BMP280
import MAX1720x

def main():
	sensor = MAX1720x.MAX1720x()

	print sensor.get_voltage()

	time.sleep(1)

if __name__ == '__main__':
	while 1:
		main()

