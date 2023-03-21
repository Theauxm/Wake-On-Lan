# Wake-On-Lan
Uses a Python Flask server to run Wake on Lan on a given MAC Address


# Installation

`python -m pip install wakeonlan flask configparser`

Copy `config.ini.example` into a new file named `config.ini`. Change the MAC Address to the computer you'd like to Wake On LAN.

# Setup

`python server.py`


# Usage

Simply visit http://localhost:5000/wake/desktop

NOTE: Change `localhost` to host computer, and `desktop` to name of section in `config.ini`.