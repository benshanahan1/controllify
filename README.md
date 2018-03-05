# Controllify v0.1
Benjamin Shanahan, 6 January 2017.



## Overview

Controllify was created in an attempt to create a programmatic remote-control of Spotify. It controls Spotify by 1) interacting with Spotify's local HTTP server and sending it commands so that Spotify responds (i.e. playing a specific track or playlist given its URI), and 2) emulating keyboard commands manually mapped to Spotify via Toastify (an application that integrates system-wide hotkeys with Spotify actions). Through this dual-approach, Controllify can control song playback through Spotify programmatically on a Windows machine.

UART was used for the command interface because this project was initially designed to be a command-server for a physical Arduino-powered switchbox that would send commands via UART to a computer running Controllify. The UART in this scenario could easily be swapped out with a wireless protocol for a more mobile Controllify-switchbox.

Before getting started, please check that you have installed all dependencies (DEPENDS.md).



## Getting started

To run Controllify virtually (without switchbox hardware), you need to install a COM port emulator (i.e. com0com). Once installed, create COM ports 4 and 5 and link them together so that a bytes written to one will appear on the other. Once done, launch the Controllify server (Controllify.bat) and the TX emulator (/emulator/launch_tx.bat). Inside of the emulator, try the following commands and if everything is working properly, Spotify should respond:

* play
* next
* prev
* volup
* voldown
* visible
* mute

Additionally, you can paste a Spotify URI directly into the emulator (to copy the URI, right-click a song, playlist, album, etc. in Spotify Desktop and select 'Copy Spotify URI'). Doing so will play the given track in Spotify Desktop.

Please note that for most of the functionality of this application, the keyboard shortcuts called by Controllify must correspond to those defined in Toastify. The Toastify hotkeys should be set so that they match the actions defined below (or these actions can be changed in keyboard.py):

| Action         | Shortcut       |
|----------------|----------------|
| Play / Pause   | Ctrl-Alt-Up    |
| Next Track     | Ctrl-Alt-Right |
| Previous Track | Ctrl-Alt-Left  |
| Show / Hide    | Ctrl-Alt-Down  |
| Mute           | Ctrl-Alt-F10   |
| Volume Down    | Ctrl-Alt-F11   |
| Volume Up      | Ctrl-Alt-F12   |
