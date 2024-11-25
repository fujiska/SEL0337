
from gpiozero import RGBLED
from time import sleep

led = RGBLED(red = 9, green = 10, blue = 11)

def fade_to_color(start_color, end_color, steps=50, delay=0.05):
	for step in range(steps+1):
		r = start_color[0] + (end_color[0] - start_color[0]) * step/steps
		g = start_color[1] + (end_color[1] - start_color[1]) * step/steps
		b = start_color[2] + (end_color[2] - start_color[2]) * step/steps
		led.color = (r,g,b)
		sleep(delay)

fade_to_color((0,0,0),(1,0,0))
fade_to_color((1,0,0),(0,1,0))
fade_to_color((0,1,0),(0,0,1))
fade_to_color((0,0,1),(1,1,0))
fade_to_color((1,1,0),(0,1,1))
fade_to_color((0,1,1),(1,0,1))
fade_to_color((1,0,1),(1,1,1))
fade_to_color((1,1,1),(1,0,0))

