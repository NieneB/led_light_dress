from flask import Flask, render_template, request
from thread import start_new_thread
import os

app = Flask(__name__)

CurrentSignal = "White"

@app.route('/', methods=['GET'])

def Main():
	global CurrentSignal

	if request.args.get('Signal'):
		CurrentSignal=request.args.get('Signal')
                if CurrentSignal=='P1':
                    print 'P1'
                    os.system("python /home/pi/led_light_dress/my_python/button.py")
                if CurrentSignal=='P2':
                    print 'P2'
                    os.system("sudo python /home/pi/led_light_dress/rpi_ws281x/python/examples/strandtest.py") 
	return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
