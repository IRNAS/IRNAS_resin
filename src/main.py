import time

import BMP280
import MAX1720x
import BQ2429x

import Adafruit_GPIO.I2C as I2C
i2c = I2C

address = 0x36

def main():

	'''combined = _device.readU16(0x08)
	value = combined / 256'''

	combined = _device.readU16(0x09)
	value = combined * 0.078125

	print value

	time.sleep(1)

if __name__ == '__main__':

	_device = i2c.get_i2c_device(address)

	while 1:
		main()

