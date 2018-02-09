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

ALL_LED = strip1 + strip2 + strip3 +strip4 + strip5 + strip6 +strip7+ strip8 + strip9 +strip10+ topR + topL


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


def oneColor(strip,color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

def rainbow(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(ALL_LED[i], wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

try:
    while(True):
    	rainbow(strip)

except(KeyboardInterrupt, SystemExit):
    print "stop"
    oneColor(strip, Color(0,0,0))

