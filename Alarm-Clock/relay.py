from gpiozero import LED
from time import sleep

trigger = LED(4)

sleep(3)
trigger.on()
sleep (3.0)
trigger.off()
sleep (3.0)
trigger.on()
sleep(3.0)
trigger.off()

