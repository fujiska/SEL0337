# O código faz o buzzer apitar uma única vez
from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)
buzz = True # Variável de controle para executar o loop

while buzz: # Loop que será executado enquanto "buzz" for True
	buzzer.on()  # Ativa o buzzer (emite som)
	sleep(1)     # Aguarda 1 segundo com o som ligado
	buzzer.off() # Desativa o buzzer
	sleep(1)     # Aguarda 1 segundo com o som desligado
	buzz = False # Define "buzz" como False para encerrar o loop
