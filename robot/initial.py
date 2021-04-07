from gpiozero import LED
from time import sleep
from controller import robot_controller
import os

control = robot_controller(os.path.dirname(os.path.realpath(__file__)))

for pin in control.get_config()['Robot']:
    re = LED(pin)

led = LED(5)

led.blink()
sleep(1)
