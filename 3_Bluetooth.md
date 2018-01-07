# Setting up Bluetooth connection


	sudo apt-get install bluetooth python-gobject python-gobject-2 blueman bluez python-bluetooth 

	sudo reboot

	sudo bluetoothctl


	[bluetooth]# power on
	[bluetooth]# agent on
	[bluetooth]# discoverable on
	[bluetooth]# pairable on
	[bluetooth]# scan on

	pair <adress phone>

