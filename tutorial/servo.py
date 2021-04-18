from gpiozero import Servo
from time import sleep

servo = Servo(18)

while True:
    servo.min()
    sleep(0.1)
    servo.mid()
    sleep(0.1)
    servo.max()
    sleep(0.1)