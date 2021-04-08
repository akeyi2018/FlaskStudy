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

    def set_robot_info(self, direction):
        try:
            with open(self.robot_info, 'r') as json_file:
                json_data = json.load(json_file)
                json_data['direction'] = direction
        
            with open(self.robot_info , 'w') as json_file:
                json.dump(json_data, json_file, indent=4)
        except:
            pass
class MoveBody:
    def __init__(self, pins):
        self.robot = Robot(left=(pins[0],pins[1]), right=(pins[2], pins[3]))

    def run(self, direction):
        actions = {
            0 : self.robot.stop,
            1 : self.robot.forward,
            2 : self.robot.backward,
            3 : self.robot.left,
            4 : self.robot.right,
        }
        actions[direction]()
        sleep(0.1)

if __name__ == '__main__':
    control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
    movebody = MoveBody(control.get_config()['Robot'])
    movebody.run(1)
    movebody.run(2)
    