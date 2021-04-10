import RPi.GPIO as GPIO
from time import sleep
import json, os
from gpiozero import DistanceSensor, LED
from signal import pause

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
        GPIO.setup(self.pinList, GPIO.OUT)

    def run(self, direction, tm):
        # if led.value == 1 :
        #     print('1') 
        #     return
        actions = {
            0 : [0,0,0,0],
            1 : [1,0,1,0],
            2 : [0,1,0,1],
            3 : [0,1,1,0],
            4 : [1,0,0,1],
        }
        for pin, val in zip(self.pinList, actions[direction]):
            GPIO.output(pin, val)
        sleep(tm)

class SensingDistance():
    def __init__(self):
        self.sensor = DistanceSensor(27, 17, max_distance=1, threshold_distance=0.1)

    def run(self, direction, tm):
        self.led = led

        self.control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
        self.movebody = MoveBody(control.get_config()['Robot'])

        self.sensor.when_deactivated = self.movebody.run(direction, tm)
        self.sensor.when_activated = self.movebody.run(0, 0.001)
        # pause() 

if __name__ == '__main__':
    
    sensor = SensingDistance()
    sensor.run(1,5)
    
  
    