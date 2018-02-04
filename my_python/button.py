from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

button1=13
button2=15

GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)


while(1):
    if GPIO.input(button1)==0:
        print "Button 1 pressed"
        sleep(0.8)
    if GPIO.input(button2)==0:
        print "Button 2 pressed"
        sleep(0.8)

