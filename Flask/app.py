from flask import Flask, redirect, render_template, request, session, url_for, Response, jsonify
import sqlite3
import json
import subprocess
import os 
from werkzeug.serving import run_simple
from werkzeug.middleware.proxy_fix import ProxyFix
import requests


##settings 

# set here the IP address if run on your pc
ip_address = 'localhost'
# ip_address = '192.168.1.1'

##settings 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
app = Flask(__name__, static_url_path='')

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)
os.chdir(dir_path)

proxies = {
 "http": None,
 "https": None,
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SERVING FUNCTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/pacman/')            
def index():
    return app.send_static_file('pacman/index.html')

##server start

if __name__ == '__main__':
  

    if "SNAP_DATA" in os.environ:
        run_simple('unix://'+os.environ['SNAP_DATA']+'/package-run/pacman/example.sock', 0, app)
        #app.run(host='0.0.0.0',debug = False, port=3125)
    else:

        app.run(host='0.0.0.0',debug = False, port=12121)

