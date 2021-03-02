from gpiozero import LED
from time import sleep

trigger = LED(4)

trigger.on()
sleep (1.0)
trigger.off()
sleep (1.0)
trigger.off()