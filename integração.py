"Integração da câmera com o Led"
import time
import board
import neopixel
import RPi.GPIO as GPIO
from picamera import PiCamera

"Configurando o Led"
pixel_pin = board.D18
num_pixels = 16
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False,
                           pixel_order=ORDER)
                           
"Configurando a camera"
camera = PiCamera()
camera.start_preview()
time.sleep(5)
"Integração"

x = 0
y = 0
z = 0
if x == 0:
	pixels.fill((255,0,0))
	pixels.show()
	camera.capture('/home/clemilton/Desktop/LedVermelho.jpg')
	time.sleep(0.5)
	x+=1
	if x == 1:
		pixels.fill((0, 255, 0))
		pixels.show()
		camera.capture('/home/clemilton/Desktop/LedVerde.jpg')
		time.sleep(0.5)
		y+=1
		if x == 1 & y == 1:
			pixels.fill((0,0,255))
			pixels.show()
			camera.capture('/home/clemilton/Desktop/LedAzul.jpg')
			time.sleep(0.5)
			y = 2
			x = 2
			z +=1
			if z == 1:
				pixels.fill((0,0,0))
				pixels.show()
				time.sleep(0.5)
				x = 0
				y = 0
				z = 0
				camera.stop_preview()
