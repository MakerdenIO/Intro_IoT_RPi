"""
  09/01/2015
  Author: Makerbro
  Platforms: Raspberry Pi (Raspbian)
  Language: Python
  File: application.py
  ------------------------------------------------------------------------
  Description: 
  ------------------------------------------------------------------------
  Please consider buying products from ACROBOTIC to help fund future
  Open-Source projects like this! We'll always put our best effort in every
  project, and release all our design files and code for you to use. 
  https://acrobotic.com/
  ------------------------------------------------------------------------
  License:
  Beerware License; if you find the code useful, and we happen to cross 
  paths, you're encouraged to buy us a beer. The code is distributed hoping
  that you in fact find it useful, but  without warranty of any kind.
"""
# -----------------------------------------------------------------------------
# GPIO
# -----------------------------------------------------------------------------
import RPi.GPIO as GPIO                 # Import GPIO library
import time                             # Import time library for sleep delay

led_pin = 7                             # Pin number for LED
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

# -----------------------------------------------------------------------------
# API
# -----------------------------------------------------------------------------
# Use the route() decorator to tell Flask what URL should trigger our function
from flask import Flask, render_template 
app = Flask(__name__)                       # Instantiate a Flask object
@app.route('/')                 
def index():              
    templateData = {
        'title' : 'Welcome to the web-led control center',
        'usage' : 'API can be accessed via "http://host/on"'
    }
    return render_template('main.html', **templateData)

@app.route('/on', methods=['GET'])
def rpi_on():
    GPIO.output(led_pin,True)   # Turn on GPIO pin "led_pin"
    # On a GET request the HTTP server must return something. The HTTP 
    # 'empty response' response is 204 No Content.
    return ('', 204)
 
@app.route('/off', methods=['GET'])
def rpi_off():
    GPIO.output(led_pin,False)  # Turn on GPIO pin "led_pin"
    return ('', 204)

# use the run() function to run the local server with our application
if __name__ == '__main__':
    try: 
        app.run(host='0.0.0.0',debug=True)      # Accessible from the outside world
    except KeyboardInterrupt:  
        print "Quiting..."  
    finally:  
        GPIO.cleanup() # this ensures a clean exit   
