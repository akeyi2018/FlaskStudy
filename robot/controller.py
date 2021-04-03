from gpiozero import Robot
from time import sleep
import json, os

class robot_controller:
    def __init__(self, path):
        self.path = path
        self.robot_info = os.path.join(self.path, 'robot_info.json')
        self.config = os.path.join(self.path, 'config.json')
    
    def get_config(self):
        with open(self.config,  mode='r', encoding='utf-8') as json_file:
            return json.load(json_file)

class MoveBody:
    def __init__(self, LEFT_PIN_1, LEFT_PIN_2, RIGHT_PIN_1, RIGHT_PIN_2):
        self.robot = Robot(left=(LEFT_PIN_1,LEFT_PIN_2), right=(RIGHT_PIN_1, RIGHT_PIN_2))

    def run(self, direction):
        actions = {
            0 : self.robot.stop,
            1 : self.robot.forward,
            2 : self.robot.backward,
            3 : self.robot.left,
            4 : self.robot.right,
        }
        actions[direction]()
        sleep(0.5)

if __name__ == '__main__':
    movebody = MoveBody(6,13,19,26)
    movebody.run(1)
    movebody.run(2)
    