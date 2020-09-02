from smbus2 import SMBus, i2c_msg
from nau7802 import *
from os import system
from time import sleep

bus = SMBus(1)

boot_cycle(bus)
print('Sensor Booted!')
sleep(1)
set_avdd_voltage(bus, '3.3v')
select_avdd_source(bus, internal_source=True)
set_conversion_rate(bus, conversion_rate='sps10')
set_gain(bus, 'x1')
start_reading_data(bus, start=True)

while True:
    system('clear')
    print('Current Load: {}'.format(read_load(bus)))
    sleep(0.5)
