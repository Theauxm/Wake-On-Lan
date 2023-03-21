# Wake-On-Lan
Uses a Python Flask server to run Wake on Lan on a given MAC Address. I use this on a Raspberry Pi in conjunction with a Tailscale VPN to be able to turn on my computer remotely.

I have the server run on startup, and will give details on how to do that below from a RPi.


# Installation

`python -m pip install wakeonlan flask configparser`

Copy `config.ini.example` into a new file named `config.ini`. Change the MAC Address to the computer you'd like to Wake On LAN.

# Setup

To run the server simply run the file:
`python server.py`



If you'd like to run the file on startup, edit `/etc/rc.local`.

`sudo vim /etc/rc.local`

Append the following to the end of the file:

`python /path/to/server.py`

`exit 0`

Reboot the RPi and the server should be running:

`sudo reboot`


# Usage

Simply visit http://localhost/wake/desktop

NOTE: Change `localhost` to host computer, and `desktop` to name of section in `config.ini`.

NOTE: You will need to append the port (e.g. `:5000`) to the end of the hostname (in our case `localhost`) if you change the port.
