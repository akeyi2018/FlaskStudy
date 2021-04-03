from gpiozero import Robot
from time import sleep
robot = Robot(left=(6,13), right=(19,26))

robot.forward()
sleep(3)

robot.backward()
sleep(3)

robot.left()
sleep(3)

robot.right()
sleep(3)
