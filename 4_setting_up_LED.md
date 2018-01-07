# LED strips

## LED strip specifications:
ws2812 DC 
5V ip65 Waterproof 
30 leds/m
power: 9 watt/meter
width:10mm height:2.5mm

FPCB JST-SM connectoren.

Ordered from: https://nl.aliexpress.com/item/DC-5V-12V-WS2811-WS2812B-WS2812-IC-SMD-5050-digital-RGB-Strip-waterproof-Dream-Magic-Full/32823280011.html?spm=2114.search0104.8.3.SI6cRu

Verbruik: 2Amp per meter when fully lit. 1 when programmed. 0.5 when programmed less bright. 

## What to install:

	sudo apt-get install build-essential python-dev unzip wget scons swig

	wget https://github.com/jgarff/rpi_ws281x/archive/master.zip && unzip master.zip && cd rpi_ws281x-master && sudo scons && cd python && sudo python setup.py install

From https://dordnung.de/raspberrypi-ledstrip/ws2812

## Testing

The variable LED_COUNT is set to the total number of LED chips on the LED-Strip

Then the test is started with:

	sudo python strandtest.py