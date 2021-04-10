import RPi.GPIO as GPIO
from time import sleep
import json, os
from gpiozero import DistanceSensor, LED
from signal import pause

led = LED(5)

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
        if led.value == 1:
            print('1')
            return
        else:
            print('0') 
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
    def __init__(self, callback1):
        self.sensor = DistanceSensor(27, 17, max_distance=1, threshold_distance=0.1)
        self.callback1 = callback1

    def run(self):
        self.sensor.when_deactivated = led.on 
        self.sensor.when_activated = led.off
        self.callback1(led.value)
        # pause() 


def OK(val):
    print('OK{}', val)

def NG(val):
    print('NG{}', val)

if __name__ == '__main__':
    control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
    movebody = MoveBody(control.get_config()['Robot'])
    sensor = SensingDistance(OK)
    sensor.run()
    # for _ in range(5):
    #     movebody.run(1, 1)
    # movebody.run(2, 1)
    # movebody.run(0,0.001)
   
    