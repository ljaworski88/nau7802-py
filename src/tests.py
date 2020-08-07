from smbus2 import SMBus, i2c_msg
from nau7802 import *
from os import system
from time import sleep

bus = SMBus(1)

boot_cycle(bus)
print('Sensor Booted!')
sleep(1)

while True:
    system('clear')
    print('Current Load: {}'.format(read_load(bus)))
    sleep(0.5)
