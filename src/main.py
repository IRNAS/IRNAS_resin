import time

import BMP280

def main():
	sensor = BMP280.BMP280()
	print sensor.read_temperature()
	print ""
	print sensor.read_pressure()
	time.sleep(1)

if __name__ == '__main__':
	main()

