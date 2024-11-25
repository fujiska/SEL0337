from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)
buzz = True
while buzz:
	buzzer.on()
	sleep(1)
	buzzer.off()
	sleep(1)
	buzz = False
