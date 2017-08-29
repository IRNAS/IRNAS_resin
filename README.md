# IRNAS battery pack Raspberry Pi support
This project extends the [IRNAS battery pack ](https://github.com/IRNAS/IoT-battery-pack) project with the [Raspberry Pi](https://www.raspberrypi.org/) running [resin.io](https://resin.io/).

Purpose of this project is to make the battery pack easily accessable and controllable through [resin.io](https://resin.io/).

## Supported sensors
 - ***BQ2429***
 - ***MAX1720***

## Main files

#### BQ2429x.py
Python script for connecting to the BQ2429 chip and interfacing with it.

```__init__()``` - connects to the device through the I2C module

```get_status(type_of_status)``` - reads out the ***status*** register and returning data dependent on the ***type_of_status*** parameter

```get_faults(type_of_fault)``` - reads out the ***faults*** register and returning data dependent on the ***type_of_fault*** parameter

```set_ter_prech_current(termination, precharge)``` - writes data to the ***term/prech*** register

```set_charge_voltage(c_v_l, precharge, thresh)``` - writes the data to the ***voltage charge*** register

#### MAX1720.py
Python script for connecting to the MAX1720 chip and interfacing with it.

```__init__()``` - conects to the device through the I2C module

```get_cell_voltage()``` -  gets the lowest cell voltage

```get_max_voltage()``` - gets the max voltage the cell was on since reset

```get_current()``` - get the current running from the cells

```get_avg_current()``` - get the average current consumption

```get_maxmin_current()``` - get the max and minimum current since reset

```get_temperature()``` - get the current temperature

```get_SOC()``` - get a percentage of the capacity

```get_capacity()``` - get the capacity

```get_TTE()``` - get the estimated time to empty

```get_TTF()``` - get the estimate time to full

```get_battery_absent()``` - checks if the battery is absent or not

```reset_minmax_current()``` - reset the minmax values (sets the minmax register to default)

```set_average_current_update_time(value)``` - sets the average current monitoring time
