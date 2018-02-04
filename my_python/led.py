
from neopixel import *
TOTAL_LED_COUNT = 150
strip = Adafruit_NeoPixel(TOTAL_LED_COUNT, 18, 800000, 5, False, 255)
strip.begin()
strip.setPixelColorRGB(LED_CHIP_NUMBER, R, G, B)
strip.show()
