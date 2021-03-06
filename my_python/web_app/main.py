from flask import Flask, render_template, request
from thread import start_new_thread
import os
print os.getenv("USER")
print os.getenv("SUDO_USER")

from neopixel import *
import time

COLOR= Color(255,10,20)
LED_COUNT = 162
BR= 100

strip = Adafruit_NeoPixel(LED_COUNT, 18, 800000)
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
topL = range(153,159)
topR= range(159,165)

strip2.reverse()
strip4.reverse()
strip6.reverse()
strip8.reverse()
strip10.reverse() 
topR.reverse()

ALL_LED_TOP = strip1 + strip2 + topR + strip3 +strip4 + strip5 + strip6 +strip7+ strip8 + strip9 +strip10 + topL
ALL_LED = strip1 + strip2 + strip3 +strip4 + strip5 + strip6 +strip7+ strip8 + strip9 +strip10
ALL_STRIP_MATRIX = [strip1, strip2,strip3,strip4, strip5 ,strip6,strip7,strip8, strip9,strip10]

LOW_LED = strip1[12:15] + strip2[12:15] + strip3[12:15] +strip4[12:15] + strip5[12:15] + strip6[12:15] +strip7[12:15]+ strip8[12:15] + strip9[12:15] +strip10[12:15]

strip.setBrightness(BR)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=15):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(LED_COUNT):
			if LED_COUNT==150:
				strip.setPixelColor(ALL_LED[i], wheel((int(i * 256 / LED_COUNT) + j) & 255))
			else:
				strip.setPixelColor(ALL_LED_TOP[i],wheel((int(i * 256 / 162) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

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

def lowEnergy(strip, color, wait_ms=300, iterations=15):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, 30, 3):
				strip.setPixelColor(LOW_LED[i]+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, 30, 3):
				strip.setPixelColor(LOW_LED[i]+q, 0)

def oneColor(strip,color):
	for i in range(LED_COUNT):
		strip.setPixelColor(i, color)
	strip.show()

app = Flask(__name__)
CurrentSignal = "OFF"
@app.route('/', methods=['GET', 'POST'])

def Main():
	global CurrentSignal
	global LED_COUNT
	global COLOR
	if request.args.get('Signal'):
		CurrentSignal=request.args.get('Signal')
		# Setting top aan uit
		if CurrentSignal=='topje':
			if (LED_COUNT==150):
				LED_COUNT = 168
			else:
				LED_COUNT=150
		if CurrentSignal=='OFF':
			oneColor(strip,Color(0,0,0))
                if CurrentSignal=='a':
			strip.setBrightness(10)
                        strip.show()
		if CurrentSignal=='b':
			strip.setBrightness(50)
                        strip.show()
		if CurrentSignal=='c':
			strip.setBrightness(100)
                        strip.show()
		if CurrentSignal=='d':
			strip.setBrightness(255)
                        strip.show()
		if CurrentSignal=='P1':
			oneColor(strip,Color(0,0,0))
			colorWipe(strip,Color(255,0,10))
			colorWipe(strip,Color(0,0,0))
			colorWipe(strip,Color(255,0,10))
			colorWipe(strip,Color(0,0,0))
			colorWipe(strip,Color(255,0,10))
			colorWipe(strip,Color(0,0,0))
		if CurrentSignal=='P2':
			oneColor(strip,Color(0,0,0))
			for i in range(10):
				lowEnergy(strip,Color(255,10,20))
		if CurrentSignal=='P3':
			oneColor(strip,Color(0,0,0))
	                rainbow(strip)
                if CurrentSignal=='red':
			COLOR=Color(255,0,0)
			oneColor(strip,COLOR)
		if CurrentSignal=='blue':
			COLOR=Color(0,0,255)
			oneColor(strip,COLOR)
		if CurrentSignal=='green':
			COLOR=Color(0,255,0)
			oneColor(strip,COLOR)
		if CurrentSignal=='pink':
			COLOR=Color(255,20,20)
			oneColor(strip,COLOR)
	return render_template('index.html')


if __name__ == "__main__":
	app.run(host="0.0.0.0")
