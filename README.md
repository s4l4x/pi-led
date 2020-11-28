# pi-led
Get up and running programming LEDs like the NeoPixels from Adafruit using a Raspberry Pi and Python. Using the Raspberry Pi may not be the most power efficient, but it has built in wifi, which will save time. So if power isn't a consideration, this is an amazing way to get started quickly.

### Run the program
`sudo python3 neospark.py`

### Run on startup
1. Create a service

`nano /etc/systemd/system/neopixels.service`

2. Edit the service
```[Unit]
Description=NeoPixels Startup Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 neospark.py
WorkingDirectory=/home/pi/Desktop/pi-led
StandardOutput=inherit
StandardError=inherit
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

3. Start the service

`sudo systemctl start neopixels.service`

### Restart after editing

`sudo systemctl restart neopixels.service`
