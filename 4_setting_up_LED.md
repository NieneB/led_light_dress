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
30 LEDs: 9 Watts (about 1.8 Amps at 5 Volts).


## Hardware
 
Level shifter:

SN74AHCT125N

Specs: https://cdn-shop.adafruit.com/product-files/1787/1787AHC125.pdf


## Software 

What to install:

	sudo apt-get install build-essential python-dev unzip wget scons swig

	wget https://github.com/jgarff/rpi_ws281x/archive/master.zip && unzip master.zip && cd rpi_ws281x-master && sudo scons && cd python && sudo python setup.py install

From https://dordnung.de/raspberrypi-ledstrip/ws2812

## Testing

The variable LED_COUNT is set to the total number of LED chips on the LED-Strip

Then the test is started with:

	sudo python strandtest.py


serieof parralel schAKELEN


serie 
stroom apart 
lus voor data
?? kan dat? 

## Making it portable

2 lead accus. of 6 volt, 4.5AH

**Specs:** 
Part Number: UL4.5-6
Length: 70 ± 2 mm (2.76 inches)
Width: 47 ± 2 mm (1.85 inches)
Container Height: 101 ± 2 mm (3.94inches)
Total Height (with terminal) : 106 ± 2 mm (4.17 inches)
Approx Weight: Approx 0.75kg (1.65lbs)

Diode ? 


If your microcontroller and NeoPixels are powered from two different sources (e.g. separate batteries for each), there must be a ground connection between the two.
https://learn.adafruit.com/adafruit-neopixel-uberguide/best-practices

Lower voltages are always acceptable, 

 I need to power LOTS of NeoPixels and don’t have a power supply that large. Can I use several smaller ones?
Maybe. There are benefits to using a single supply, and large power supplies are discussed below. “Non-optimal” doesn’t necessarily mean “pessimal” though, and we wouldn’t discourage anyone from using what resources they have.

If you go this route, the key is to have all of the ground pins among the strips connected in common, but the +5V from each power supply should be connected only to one length of NeoPixels — those should not all be joined. Every power supply is a little different — not precisely 5 Volts — and this keeps some from back-feeding into others.

Pro Tip: NeoPixels don’t care what end they receive power from. Though data moves in only one direction, electricity can go either way. You can connect power at the head, the tail, in the middle, or ideally distribute it to several points. For best color consistency, aim for 1 meter or less distance from any pixel to a power connection. With larger NeoPixel setups, think of power distribution as branches of a tree rather than one continuous line.

## Limits

control up to 450 LEDs 