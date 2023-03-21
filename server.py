from flask import Flask
from wakeonlan import send_magic_packet
from configparser import ConfigParser

CONFIG_FILE_NAME = "config.ini"
FLASK_PORT = 80

config = ConfigParser()
config.read(CONFIG_FILE_NAME)

app = Flask(__name__)

def main():
    app.run(port=FLASK_PORT)


@app.route('/wake/<name>')
def wake(name):
    try:
        mac = config.get(name, "mac")
        send_magic_packet(mac)
        return "OK"
    except:
        return "NOT OK"


if __name__ == "__main__":
    main()