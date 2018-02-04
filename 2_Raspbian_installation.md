# Raspberry PI installation

I installed Raspbian Stretch Lite. This because I won't be using any Desktop interface. I connect to the Rapsberry with SSH on my laptop, since I already have experience with this and have no separate screen available.
  
### 1. Format SD card and install Raspbian.
I formatted my SD card and installed the Raspbian image on it. For the formatting I followed the steps from: https://www.pcworld.com/article/3176712/linux/how-to-format-an-sd-card-in-linux.html.

Then downloaded the image from https://www.raspberrypi.org/downloads/raspbian/
Using Etcher I wrote this to the SD card, as described in the installation guide. https://www.raspberrypi.org/documentation/installation/installing-images/README.md

### 2. Connecting through SSH
In order to be able to connect through SSH I needed to enable it first on the SD card. So still having the SD card in my laptop, I added a file named `ssh` without any extension or content on the boot partition of the SD card. Now connecting the PI to my network directly into my router with a ether cable, SSH is enabled.  

From my laptop, through the wifi network, I detected the IP address of my PI.

Getting own ip adres:

	ifconfig

Scanning form available ip adresses:

	nmap -sn <IPadres>

See: https://www.raspberrypi.org/documentation/remote-access/ip-address.md

Then with ssh we can connect to it.

	ssh pi@<IPadress> 

Default login password is `raspberry`.

First things first! Change the Password and update the system!

	password
	sudo apt-get update
	sudo apt-get upgrade

	sudo apt-get install build-essential git vim

Get this repro:

	git clone https://github.com/NieneB/led_light_dress.git

## Reducing power consumption
Add `/usr/bin/tvservice -o` to /etc/rc.local


## Clean shutdown raspberry pi

Clean shutdown: 

	sudo shutdown -h now
