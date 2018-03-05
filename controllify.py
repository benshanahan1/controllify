"""
Controllify
Benjamin Shanahan, 6 January 2017.

Receives information from a given COM port and then triggers Spotify in various ways.
This includes combining functionality provided by the Play button (Web Interface) and
by the third-party application Toastify (https://toastify.codeplex.com/). Functionality
provided includes pausing / playing music, showing / hiding the spotify window, going to
previous / next tracks, and changing and muting the system volume.
"""

import serial
import keyboard as kb
import webcontroller

class Controllify:

    def __init__(self, port="COM3", baud=9600):
        self.port    = port
        self.baud    = baud
        self.spotify = webcontroller.WebController()  # establish connection with Spotify Desktop and open it if needed
        self.com     = serial.Serial(self.port, self.baud, timeout=0)  # establish COM port connection

    """ Receive incoming information from COM port """
    def rx(self):
        return self.com.readline()

    """ Send information to COM port """
    def tx(self, msg):
        self.com.write(msg)

    """ Act on command contained in parameter 'data' """
    def act(self, data=None):
        if data is not None:
            if data == "play":
                print "Toggle playback."
                kb.CtrlAltUp()
            elif data == "visible":
                print "Toggle window visibility."
                kb.CtrlAltDown()
            elif data == "next":
                print "Next track."
                kb.CtrlAltRight()
            elif data == "prev":
                print "Previous track."
                kb.CtrlAltLeft()
            elif data == "volup":
                print "Increase volume."
                kb.CtrlAltF12()
            elif data == "voldown":
                print "Decrease volume."
                kb.CtrlAltF11()
            elif data == "mute":
                print "Mute volume."
                kb.CtrlAltF10()
            elif data[:8] == "spotify:":
                print "Playing new URI (%s)." % data
                self.spotify.play(data)
            else:
                print "Unrecognized command."
            data = None  # reset data variable (not sure if necessary)