from smbus2 import SMBus, i2c_msg
from ctypes import c_int32
from time import sleep

sensor_address = 0x2A

com_mode = {'disabled' : 0b00,
            'refn'     : 0b10,
            'refp'     : 0b11}

register_address = {'PU_CTRL'     : 0x00,
                    'CTRL1'       : 0x01,
                    'CTRL2'       : 0x02,
                    'CH1_OFFSET'  : 0x03,
                    'CH1_GOFFSET' : 0x06,
                    'CH2_OFFSET'  : 0x0A,
                    'CH2_GOFFSET' : 0x0D,
                    'I2C_CTRL'    : 0x11,
                    'ADC_RESULT'  : 0x12,
                    'ADC_REG'     : 0x15,
                    'OTP_READ'    : 0x15,
                    'PGA_REG'     : 0x1B,
                    'PWR_CTRL'    : 0x1C}

def select_AVDD_source(i2c_bus, internal_source=False):
    curent_register_val = read_register(i2c_bus, 'PU_CTRL')
    new_register_val = (curent_register_val & 0b01111111) | (internal_source << 7)
    set_register(i2c_bus, 'PU_CTRL', new_register_val)

def selectClockSource(i2c_bus,  internal_source = True):
    pass

def start_reading_data(i2c_bus, start=True):
    curent_register_val = read_register(i2c_bus, 'PU_CTRL')
    new_register_val = (curent_register_val & 0b11101111) | (start << 4)
    set_register(i2c_bus, 'PU_CTRL', new_register_val)

def power_analog(i2c_bus, power_up=True):
    curent_register_val = read_register(i2c_bus, 'PU_CTRL')
    new_register_val = (curent_register_val & 0b11111011) | (power_up << 2)
    set_register(i2c_bus, 'PU_CTRL', new_register_val)

def power_digital(i2c_bus, power_up=True):
    curent_register_val = read_register(i2c_bus, 'PU_CTRL')
    new_register_val = (curent_register_val & 0b11111101) | (power_up << 1)
    set_register(i2c_bus, 'PU_CTRL', new_register_val)

def register_reset(i2c_bus, reset=True):
    curent_register_val = read_register(i2c_bus, 'PU_CTRL')
    new_register_val = (curent_register_val & 0b11111110) | (reset)
    print(new_register_val)
    set_register(i2c_bus, 'PU_CTRL', new_register_val)

def checkPowerUp(i2c_bus):
    pass

def checkDataReady(i2c_bus):
    pass

def setRDYpinPolarity(i2c_bus,  activeHigh = True):
    pass

def set_gain(i2c_bus, gain):
    gain_select = {'x1'   : 0b000,
                   'x2'   : 0b001,
                   'x4'   : 0b010,
                   'x8'   : 0b011,
                   'x16'  : 0b100,
                   'x32'  : 0b101,
                   'x64'  : 0b110,
                   'x128' : 0b111}
    if isinstance(gain, str):
        gain = gain_select[gain]
    if isinstance(gain, int):
        pass
    curent_register_val = read_register(i2c_bus, 'CTRL1')
    new_register_val = (curent_register_val & 0b11111000) | (start << 4)
    set_register(i2c_bus, 'CTRL1', new_register_val)


def set_avdd_voltage(i2c_bus, voltage):
    voltage_select =  {'4.5v' : 0b000,
                       '4.2v' : 0b001,
                       '3.9v' : 0b010,
                       '3.6v' : 0b011,
                       '3.3v' : 0b100,
                       '3.0v' : 0b101,
                       '2.7v' : 0b110,
                       '2.4v' : 0b111}
    if isinstance(voltage_select, str):
        voltage = voltage_select[voltage]
    if isinstance(register, int):
        pass
    curent_register_val = read_register(i2c_bus, 'CTRL1')
    new_register_val = (curent_register_val & 0b11000111) | (start << 4)
    set_register(i2c_bus, 'CTRL1', new_register_val)

def set_channel(i2c_bus,  channel):
    curent_register_val = read_register(i2c_bus, 'CTRL2')
    new_register_val = (curent_register_val & 0b01111111) | (channel << 7)
    set_register(i2c_bus, 'CTRL2', new_register_val)

def set_conversion_rate(i2c_bus, conversion_rate):
    sample_rate = {'sps10'  : 0b000,
                   'sps20'  : 0b001,
                   'sps20'  : 0b001,
                   'sps20'  : 0b001,
                   'sps320' : 0b111}
    if isinstance(conversion_rate, str):
        conversion_rate = sample_rate[conversion_rate]
    if isinstance(gain, int):
        pass
    curent_register_val = read_register(i2c_bus, 'CTRL2')
    new_register_val = (curent_register_val & 0b10001111) | (conversion_rate << 4)
    set_register(i2c_bus, 'CTRL2', new_register_val)

def set_calibration_mode(i2c_bus, calibration_mode):
    cal_type  = {'internal' : 0b00,
                 'offset'   : 0b10,
                 'gain'     : 0b11}
    if isinstance(conversion_rate, str):
        calibration_mode = sample_rate[calibration_mode]
    if isinstance(gain, int):
        pass
    curent_register_val = read_register(i2c_bus, 'CTRL2')
    new_register_val = (curent_register_val & 0b11111100) | (calibration_mode << 4)
    set_register(i2c_bus, 'CTRL2', new_register_val)


def calibrate(i2c_bus):
    curent_register_val = read_register(i2c_bus, 'CTRL2')
    new_register_val = (curent_register_val & 0b11111011) | (calibration_mode << 4)
    set_register(i2c_bus, 'CTRL2', new_register_val)
    while read_register(i2c_bus, 'CTRL2') >> 2 & 1:
        pass
    return bool(read_register(i2c_bus, 'CTRL2') >> 3 & 1)

def set_sda_conversion_ready(i2c_bus, sda_interrupt=False):
    curent_register_val = read_register(i2c_bus, 'I2C_CTRL')
    new_register_val = (curent_register_val & 0b01111111) | (sda_interrupt << 7)
    set_register(i2c_bus, 'I2C_CTRL', new_register_val)

def set_fast_read(i2c_bus, fast_read=False):
    curent_register_val = read_register(i2c_bus, 'I2C_CTRL')
    new_register_val = (curent_register_val & 0b10111111) | (sda_interrupt << 6)
    set_register(i2c_bus, 'I2C_CTRL', new_register_val)

def i2c_pullup(i2c_bus, pullup_mode):
    pullup = {'none'   : 0b01,
              'weak'   : 0b00,
              'strong' : 0b11}
    if isinstance(pullup_mode, str):
        pullup_mode = pullup[pullup_mode]
    if isinstance(gain, int):
        pass
    curent_register_val = read_register(i2c_bus, 'I2C_CTRL')
    new_register_val = (curent_register_val & 0b11001111) | (pullup_mode << 4)
    set_register(i2c_bus, 'I2C_CTRL', new_register_val)

def short_input(i2c_bus, input_shorted=False):
    curent_register_val = read_register(i2c_bus, 'I2C_CTRL')
    new_register_val = (curent_register_val & 0b11110111) | (input_shorted << 3)
    set_register(i2c_bus, 'I2C_CTRL', new_register_val)

def set_burnout_current(i2c_bus, burnout_activated=False):
    curent_register_val = read_register(i2c_bus, 'I2C_CTRL')
    new_register_val = (curent_register_val & 0b11111011) | (burnout_activated << 2)
    set_register(i2c_bus, 'I2C_CTRL', new_register_val)

def set_read_temperature(i2c_bus, read_temperature=False):
    curent_register_val = read_register(i2c_bus, 'I2C_CTRL')
    new_register_val = (curent_register_val & 0b11111101) | (read_temperature << 1)
    set_register(i2c_bus, 'I2C_CTRL', new_register_val)

def set_bandgap_chopper(i2c_bus, activate_chopper=True):
    curent_register_val = read_register(i2c_bus, 'I2C_CTRL')
    new_register_val = (curent_register_val & 0b11111110) | (activate_chopper)
    set_register(i2c_bus, 'I2C_CTRL', new_register_val)

# def set_clock_frequency(i2c_bus, frequency):
    # curent_register_val = read_register(i2c_bus, 'ADC_REG')
    # new_register_val = (curent_register_val & 0b11111110) | (activate_chopper)
    # set_register(i2c_bus, 'I2C_CTRL', new_register_val)

def setCommonMode(i2c_bus):
    pass

def setChopClockDelay(i2c_bus):
    pass

def readOTP(i2c_bus):
    pass

def setLDOmode(i2c_bus,  highESR):
    pass

def setPGAoutputBuffer(i2c_bus):
    pass

def setPGAbypass(i2c_bus):
    pass

def setPGAinputInversion(i2c_bus,  input_inversion=True):
    pass

def setPGAchopper(i2c_bus,  pga_choper=False):
    pass

def setPGAbypassCAP(i2c_bus,  pga_bypass_cap=True):
    pass

def setMasterBiasCurrent(i2c_bus,  current):
    pass

def setADCcurrent(i2c_bus,  current):
    pass

def setPGAcurrent(i2c_bus,  current):
    pass

def setLoadCellOffset(i2c_bus):
    pass

def boot_cycle(i2c_bus):
    register_reset(i2c_bus, True)
    sleep(0.001)
    register_reset(i2c_bus, False)
    sleep(0.001)
    power_digital(i2c_bus)
    sleep(0.001)
    power_analog(i2c_bus)
    sleep(0.001)
    start_reading_data(i2c_bus, True)

def readOffset(i2c_bus,  channel = 1):
    pass

def readGOffset(i2c_bus,  channel = 1):
    pass

def read_load(i2c_bus):
    load_data = i2c_bus.read_i2c_block_data(sensor_address, register_address['ADC_RESULT'], 3)
    reading = 0
    # setting up the twos complement for the 24 bit data
    if load_data[0] << 7 & 1:
        reading = 0xFF
    for byte in load_data:
        reading = reading << 8 | byte
    return c_int32(reading).value


def read_register(i2c_bus, register):
    if isinstance(register, str):
        register = register_address[register]
    if isinstance(register, int):
        pass
    else:
        raise TypeError()
    return i2c_bus.read_byte_data(sensor_address, register)

def set_register(i2c_bus, register,  register_value):
    if isinstance(register, str):
        register = register_address[register]
    if isinstance(register, int):
        pass
    else:
        raise TypeError()
    i2c_bus.write_byte_data(sensor_address, register, register_value)

