# RX Emulator
# Requires com0com COM port emulator.
#
# Benjamin Shanahan, 5 January 2017.

import serial
import time

ser = serial.Serial("COM5", 9600, timeout=0)

while 1:
    try:
        print "Received: ", ser.readline()
        time.sleep(1)
    except:
        print "Date could not be read."
        time.sleep(1)