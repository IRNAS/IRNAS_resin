import time

import BMP280
import MAX1720x
import BQ2429x

def main():
	#sensor = BQ2429x.BQ2429x()
	#print sensor.get_status()

	sensor = MAX1720x.MAX1720x()
	print sensor

	time.sleep(1)

if __name__ == '__main__':
	while 1:
		main()

