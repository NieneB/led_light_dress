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

ALL_LED = strip1[12:15] + strip2[12:15] + strip3[12:15] +strip4[12:15] + strip5[12:15] + strip6[12:15] +strip7[12:15]+ strip8[12:15] + strip9[12:15] +strip10[12:15]


def oneColor(strip,color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()


def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(ALL_LED[i]+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(ALL_LED[i]+q, 0)

try:
    while(True):
    theaterChase(strip)

except(KeyboardInterrupt, SystemExit):
    print "stop"
    oneColor(strip, Color(0,0,0))

