"""Serial Interface for MH-Z14A CO2 sensor
Wes Lauer
October 26, 2021
Released under MIT license

This program uses a serial UART connect to read data from a
MH-Z14A carbon dioxide sensor.
"""

import time
#from machine import UART

def CO2(ser):
    """
    A function for reading the CO2 concentration.

    Parameters
    ----------
    
    ser: machine.UART
        serial UART connection
    
    Example
    -------
    
    #Example written for an esp32. 
    #Pin 21 should be connected to rx on MH-Z14A.
    #Pin 22 should be connected to tx on MH-Z14A.
    
    import machine.UART
    import CO2_MHZ14
    ser = machine.UART(2,baudrate=9600,rx=21,tx=22)
    co2 = CO2_MHZ14.CO2(ser)
    print('Carbon Dioxide ppm = %s' % co2)
    """
    
    ser.init(9600, bits=8, parity=None, stop=1)
    code = b'\xFF\x01\x86\x00\x00\x00\x00\x00\x79'
    ser.readline()
    ser.write(code)
    time.sleep(1)
    response = ser.readline()
    co2 = 256*response[2]+response[3]
    return co2
    




