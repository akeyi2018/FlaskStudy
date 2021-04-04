from gpiozero import LED
from time import sleep

leds = [6,13,19,26]

for pin in leds:
    re = LED(pin)

led = LED(5)

led.blink()
sleep(3)
