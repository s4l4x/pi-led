import board
import neopixel
import math
import adafruit_fancyled.adafruit_fancyled as fancy

# Positional offset into color palette to get it to 'spin'
offset = 1

# Colors
cBlack  = fancy.CRGB(0.0, 0.0, 0.0)
cGreen  = fancy.CRGB(0.0000, 0.9059, 0.0057)
cOrange = fancy.CRGB(0.8082, 0.4876, 0.0010)
cPurple = fancy.CRGB(0.3716, 0.0836, 0.6754)
cWhite = fancy.CRGB(1.0, 1.0, 1.0)
cYellow = fancy.CRGB(1.0, 0.85, 0)

# Palettes
pRainbow = [fancy.CRGB(1.0, 0.0, 0.0), # Red
            fancy.CRGB(0.5, 0.5, 0.0), # Yellow
            fancy.CRGB(0.0, 1.0, 0.0), # Green
            fancy.CRGB(0.0, 0.5, 0.5), # Cyan
            fancy.CRGB(0.0, 0.0, 1.0), # Blue
            fancy.CRGB(0.5, 0.0, 0.5)] # Magenta
pBraid = [0xF8EC1F, 0xE75E8D, 0x985AA1, 0x4272B6, 0x37B574, 0xB1D137, 0xFCB740]
pHaloween = [cOrange, cBlack]
pPurpleGreen = [cPurple, cPurple, cBlack, cGreen, cGreen, cBlack]
pPurpleOrange = [cPurple, cBlack, cOrange, cBlack]
pThanksgiving = [cOrange, cYellow, cBlack, cYellow, cOrange]

palette = pThanksgiving

#-----------------------
# init
#-----------------------
pixelCount = 100
levels = (0.25, 0.3, 0.15)

pixels = neopixel.NeoPixel(pin=board.D18, n=pixelCount, pixel_order=neopixel.RGB, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

def rotatePalette():
  global offset
  while True:
    for i in range(pixelCount):
      color = fancy.palette_lookup(palette, offset + i / pixelCount)
      color = fancy.gamma_adjust(color, brightness=0.25)
      #color = fancy.gamma_adjust(color, brightness=levels)
      pixels[i] = color.pack()

    pixels.show()
    offset += 0.005  # Bigger number = faster spin
    
def flashColor():
  toggle = True
  count = 0
  globalCount = 0
  threshold = 15
  global offset
  while True:
    count += 1
    if (count > threshold):
      count = 0
      globalCount += 1
      threshold = (math.sin(globalCount * 0.1) * 0.5 + 0.5) * 30 + 5
      if (toggle):
        pixels.fill((0, 0, 0))
      else:
        fillColor = fancy.palette_lookup(palette, offset)
        pixels.fill(fillColor.pack())
      toggle = not toggle
    pixels.show()
    offset += 0.0005 # Bigger number = faster spin

# main
rotatePalette()
# flashColor()
