import time

import BMP280
import MAX1720x
import BQ2429x

import Adafruit_GPIO.I2C as I2C
i2c = I2C

address = 0x36

def main():

	print sensor.get_cell_voltage()

	time.sleep(1)

if __name__ == '__main__':

	sensor = MAX1720x.MAX1720x()

	while 1:
		main()

