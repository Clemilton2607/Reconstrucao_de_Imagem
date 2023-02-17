# Biblioteca dos LEDS

# Importações necessárias
import time
import board
import neopixel
import RPi.GPIO as GPIO

"Definindo pinos de entrada"
"Pino de conexao Raspberry (podem ser utilizados os pinos 10, 12, 18 ou 21)"
pixel_pin = board.D18
# Numero de leds que serao controlados
num_pixels = 16

"Ordem dos pixels de cor - RGB ou GRB ( Em alguns módulos as cores verde e vermelha estao invertidas)"
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False,
                           pixel_order=ORDER)

"Led Vermelho"
#pixels.fill((255, 0, 0))
#pixels.show()

"Led Verde"
#pixels.fill((0, 255, 0))
#pixels.show()

"Led Azul"
#pixels.fill((0,255,0))
#pixels.show()

"Desligando Led"
#pixels.fill((0,0,0))
#pixels.show()

"Função para Piscar o led"

while True:
	x = 0
	y = 0
	z = 0
	if x == 0:
		pixels.fill((255,0,0))
		pixels.show()
		time.sleep(0.5)
		x+=1
		if x == 1:
			pixels.fill((0, 255, 0))
			pixels.show()
			time.sleep(0.5)
			y+=1
			if x == 1 & y == 1:
				pixels.fill((0,0,255))
				pixels.show()
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


			
		
