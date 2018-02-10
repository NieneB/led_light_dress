from flask import Flask, render_template, request
from thread import start_new_thread
import os

from neopixel import *
import time



strip = Adafruit_NeoPixel(168, 18, 800000)
strip.begin()

strip1 = range(0,15)
strip2 = range(15,30)
strip3 = range(30,45)
strip4 = range(45,60)
strip5 = range(60,75)
strip6 = range(75,90)
strip7 = range(90,105)
strip8 = range(105,120)
strip9 = range(120,135)
strip10 = range(135,150)
topL = range(159,165)
topR= range(153,159)

strip2.reverse()
strip4.reverse()
strip6.reverse()
strip8.reverse()
strip10.reverse() 
topR.reverse()

def colorWipe(strip,color, wait_ms=80):
    for i in range(0,6):
        strip.setPixelColor(topL[i],color)
        strip.setPixelColor(topR[i],color)
        strip.show()
        time.sleep(wait_ms/1000.0)
    for i in range(0,15):
        strip.setPixelColor(strip1[i], color)
        strip.setPixelColor(strip2[i], color)
        strip.setPixelColor(strip3[i], color)
        strip.setPixelColor(strip4[i], color)
        strip.setPixelColor(strip5[i], color)
        strip.setPixelColor(strip6[i], color)
        strip.setPixelColor(strip7[i], color)
        strip.setPixelColor(strip8[i], color)
        strip.setPixelColor(strip9[i], color)
        strip.setPixelColor(strip10[i], color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def oneColor(strip,color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

app = Flask(__name__)
CurrentSignal = "White"
@app.route('/', methods=['GET'])

def Main():
	global CurrentSignal

	if request.args.get('Signal'):
		CurrentSignal=request.args.get('Signal')
                if CurrentSignal=='P1':
                    print 'P1'
                    colorWipe(strip,Color(255,0,10))
                if CurrentSignal=='P2':
                    print 'P2'
                    colorWipe(strip,Color(0,0,0))
	return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
