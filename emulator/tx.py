# TX Emulator
# Requires com0com COM port emulator.
#
# Benjamin Shanahan, 5 January 2017.

import serial
import time

ser = serial.Serial("COM4", 9600, timeout=0)

while 1:
    var = raw_input(">>> ")  # prompt for input
    ser.write(var)
    if var == "exit": exit()