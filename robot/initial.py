from gpiozero import LED
from time import sleep
from controller import robot_controller
import os

robot = robot_controller(os.path.dirname(os.path.realpath(__file__)))

for pin in robot.get_config()['Robot']:
    re = LED(pin)

echo = LED(robot.get_config()['distance_sensor']['echo'])
echo.off()
trigger = LED(robot.get_config()['distance_sensor']['trigger'])
trigger.off()
signal_led = LED(robot.get_config()['distance_sensor']['signal_led'])
signal_led.blink()
sleep(1)
