
from gpiozero import RGBLED
from time import sleep

led = RGBLED(red = 9, green = 10, blue = 11)

def fade_to_color(start_color, end_color, steps=50, delay=0.05):
    """
    Função que faz uma transição suave (fade) entre duas cores no LED RGB
    - start_color e end_color: cor inicial/final como uma tupla (r, g, b), onde cada valor está entre 0 e 1
    - steps: número de passos para a transição (quanto maior, mais suave)
    - delay: tempo (em segundos) entre cada passo, controlando a velocidade da transição
    """
	for step in range(steps+1): # Loop para calcular e aplicar as cores em cada passo
		# Calcula os valores intermediários de vermelho, verde e azul usando interpolação linear
		r = start_color[0] + (end_color[0] - start_color[0]) * step/steps
		g = start_color[1] + (end_color[1] - start_color[1]) * step/steps
		b = start_color[2] + (end_color[2] - start_color[2]) * step/steps
		led.color = (r,g,b) # Atualiza a cor do LED RGB com os valores interpolados
		sleep(delay) # Pausa entre os passos para criar o efeito de fade

# Transições entre cores RGB predefinidas
fade_to_color((0,0,0),(1,0,0))
fade_to_color((1,0,0),(0,1,0))
fade_to_color((0,1,0),(0,0,1))
fade_to_color((0,0,1),(1,1,0))
fade_to_color((1,1,0),(0,1,1))
fade_to_color((0,1,1),(1,0,1))
fade_to_color((1,0,1),(1,1,1))
fade_to_color((1,1,1),(1,0,0))

