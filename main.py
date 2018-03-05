"""
Controllify Server v0.1
Benjamin Shanahan, 6 January 2017.

Listens for commands from a specified COM port and then delegates them.
"""

import time
from controllify import Controllify

print "Controllify v0.1"
print "Code by Benjamin Shanahan."
print ""

if __name__ == "__main__":
    port = "COM5"
    baud = 9600
    refresh_rate = 0.2  # in seconds

    print "Please wait, booting server."
    controller = Controllify(port, baud)  # connect to serial port

    print "Boot success. Waiting for input..."
    print ""

    while 1:
        data = controller.rx()
        
        if data == "exit": exit()
        
        if data != "" and data is not None:
            controller.act(data)
        
        time.sleep(refresh_rate)  # allow escape sequence