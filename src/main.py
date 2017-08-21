import time

import BMP280
import MAX1720x
import BQ2429x

def main():
	sensor = BMP280.BMP280()

	print sensor.read_temperature()

	time.sleep(1)

if __name__ == '__main__':


	while 1:
		main()

