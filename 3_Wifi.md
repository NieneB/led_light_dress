# Set-up WIFI

To scan for WiFi networks, use the command 
	
	sudo iwlist wlan0 scan

	sudo vim /etc/wpa_supplicant/wpa_supplicant.conf



	network={
		ssid=""
		#psk=""
		psk=
	}


	wpa_cli -i wlan0 reconfigure

	ifconfig wlan0

	sudo reboot

