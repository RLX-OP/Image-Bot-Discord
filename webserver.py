# -- Importing Packages -- #
from flask import Flask
from threading import Thread
from logging import getLogger, ERROR  


# -- Disables Flask App Logging  -- #

log = getLogger('werkzeug')
log.setLevel(ERROR)


# - Webserver Setup -- #

app = Flask('')

@app.route('/')

def home():
        return '<h1> Hosting Active </h1><p>This bot is made by RLX, So make sure to credit RLX</p><p>Join the discord server now -  https://discord.gg/SN3mZPxjEW</p>'

def run():
        app.run(host='0.0.0.0', port=8080)
        
def keep_alive():
        t = Thread(target=run)
        t.start()
