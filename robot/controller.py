import RPi.GPIO as GPIO
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
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.pinList = pins

    def run(self, direction):
        actions = {
            0 : [0,0,0,0],
            1 : [1,0,1,0],
            2 : [0,1,0,1],
            3 : [0,1,1,0],
            4 : [1,0,0,1],
        }
        for pin, val in zip(self.pinList, actions[direction]):
            GPIO.output(pin, val)
        sleep(1.0)
        GPIO.cleanup()

if __name__ == '__main__':
    control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
    movebody = MoveBody(control.get_config()['Robot'])
    movebody.run(1)
    movebody.run(2)
    