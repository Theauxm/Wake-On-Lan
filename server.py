from flask import Flask
from wakeonlan import send_magic_packet
from configparser import ConfigParser
import os

CONFIG_FILE_NAME = "config.ini"
FLASK_PORT = 80

config = ConfigParser()
app = Flask(__name__)

def main():
    # Gets absolute path for potential of running the server outside of the directory it is in.
    absolute_path = f"{os.path.dirname(os.path.abspath(__file__))}/{CONFIG_FILE_NAME}"
    config.read(absolute_path)

    # Uses 0.0.0.0 to be seen outside of localhost on the local network.
    app.run(host="0.0.0.0", port=FLASK_PORT)


@app.route('/wake/<name>')
def wake(name):
    mac = config.get(name, "mac")
    send_magic_packet(mac)
    return "OK"


if __name__ == "__main__":
    main()
