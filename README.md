# Controllify v0.1
Benjamin Shanahan, 6 January 2017.

Controllify is a server that responds to incoming COM port commands (listed below). The server then interacts directly with the Spotify application on the user's computer in order to skip songs, change volume, etc. The original concept for Controllify was that it would be used in conjunction with a physical switchbox (with an Arduino inside) that sends commands to a set COM port.

Before getting started, please check that you have installed all dependencies (depends.md).

To run Controllify virtually (without switchbox hardware), you need to install a COM port emulator (i.e. com0com). Once installed, create COM ports 4 and 5 and link them together so that a bytes written to one will appear on the other. Once done, launch the Controllify server (Controllify.bat) and the TX emulator (/emulator/launch_tx.bat). Inside of the emulator, try the following commands and if everything is working properly, Spotify should respond:

* play
* next
* prev
* volup
* voldown
* visible
* mute

Additionally, you can paste a Spotify URI directly into the emulator (right click a song, playlist, album, etc. within Spotify Desktop and click Copy Spotify URI). Doing so will play the given track in Spotify Desktop.

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
