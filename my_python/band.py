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
    on = True
    count = 0

    for i in range(0,6):
        strip.setPixelColor(topL[i],color)
        strip.setPixelColor(topR[i],color)
        strip.show()
        time.sleep(wait_ms/1000.0)
    for i in range(0,15):
        if on :
            strip.setPixelColor(strip1[i],color)
            strip.setPixelColor(strip2[i],color)
            strip.setPixelColor(strip3[i],color)
            strip.setPixelColor(strip4[i],color)
            strip.setPixelColor(strip5[i],color)
            strip.setPixelColor(strip6[i],color)
            strip.setPixelColor(strip7[i],color)
            strip.setPixelColor(strip8[i],color)
            strip.setPixelColor(strip9[i],color)
            strip.setPixelColor(strip10[i],color)
        else : 
            strip.setPixelColor(strip1[i],Color(0,0,0))
            strip.setPixelColor(strip2[i],Color(0,0,0))
            strip.setPixelColor(strip3[i],Color(0,0,0))
            strip.setPixelColor(strip4[i],Color(0,0,0))
            strip.setPixelColor(strip5[i],Color(0,0,0))
            strip.setPixelColor(strip6[i],Color(0,0,0))
            strip.setPixelColor(strip7[i],Color(0,0,0))
            strip.setPixelColor(strip8[i],Color(0,0,0))
            strip.setPixelColor(strip9[i],Color(0,0,0))
            strip.setPixelColor(strip10[i],Color(0,0,0))
        count = count +1
        strip.show()
        time.sleep(wait_ms/1000.0)
        print count
        if (count == 3):
            if on: 
                on = False
            else: 
                on = True
            count = 0
            
def oneColor(strip,color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    

try:
    while(True):
        on = False
        i = 0
        count = 0
        color = Color(255,10,10)
        wait_ms=80

        while (i < 15):
            if on :
                strip.setPixelColor(strip1[i],color)
                strip.setPixelColor(strip2[i],color)
                strip.setPixelColor(strip3[i],color)
                strip.setPixelColor(strip4[i],color)
                strip.setPixelColor(strip5[i],color)
                strip.setPixelColor(strip6[i],color)
                strip.setPixelColor(strip7[i],color)
                strip.setPixelColor(strip8[i],color)
                strip.setPixelColor(strip9[i],color)
                strip.setPixelColor(strip10[i],color)
            else : 
                strip.setPixelColor(strip1[i],Color(0,0,0))
                strip.setPixelColor(strip2[i],Color(0,0,0))
                strip.setPixelColor(strip3[i],Color(0,0,0))
                strip.setPixelColor(strip4[i],Color(0,0,0))
                strip.setPixelColor(strip5[i],Color(0,0,0))
                strip.setPixelColor(strip6[i],Color(0,0,0))
                strip.setPixelColor(strip7[i],Color(0,0,0))
                strip.setPixelColor(strip8[i],Color(0,0,0))
                strip.setPixelColor(strip9[i],Color(0,0,0))
                strip.setPixelColor(strip10[i],Color(0,0,0))
            i = i+ 1
            strip.show()
            time.sleep(wait_ms/1000.0)
            count = count +1
            print count
            while (count % 3 == 0 ):
                if on: 
                    on = False
                else: 
                    on = True
                count = count+1
        i = 0
        
except(KeyboardInterrupt, SystemExit):
    print "stop"
    oneColor(strip, Color(0,0,0))

