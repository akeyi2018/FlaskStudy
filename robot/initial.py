# from gpiozero import LED
from time import sleep
from controller import robot_controller
import os

control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
config = control.get_config()

print(control.get_config()['Robot'])

# for pin in config['Robot']:
#     re = LED(pin)

# led = LED(5)

# led.blink()
# sleep(1)
