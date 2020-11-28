# pi-led
Get up and running programming LEDs like the NeoPixels from Adafruit using a Raspberry Pi and Python. Using the Raspberry Pi may not be the most power efficient, but it has built in wifi, which will save time. So if power isn't a consideration, this is an amazing way to get started quickly.

## Setup to run on start
1. Copy the service file to etc (note the ExecStart and WorkingDirectory properties)

`cp neopixels.service /etc/systemd/system`

2. Start the service

`sudo systemctl start neopixels.service`

## Editing
If configured to run on start, restart the service: 

`sudo systemctl restart neopixels.service`

Or run manually to see compiler output:

`sudo python3 neopixels.py`
