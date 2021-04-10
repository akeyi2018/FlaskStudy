import RPi.GPIO as GPIO
from time import sleep
import json, os
from gpiozero import DistanceSensor, LED
from signal import pause
from flask import redirect, url_for

class robot_controller:
    def __init__(self, path):
        self.path = path
        self.robot_info = os.path.join(self.path, 'robot_info.json')
        self.config = os.path.join(self.path, 'config.json')
    
    def get_config(self):
        with open(self.config,  mode='r', encoding='utf-8') as json_file:
            return json.load(json_file)

    def get_robot_info(self):
        with open(self.robot_info,  mode='r', encoding='utf-8') as json_file:
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
    def set_robot_status(self, status):
        try:
            with open(self.robot_info, 'r') as json_file:
                json_data = json.load(json_file)
                json_data['status'] = status
        
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

    def run(self):
        control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
        res = control.get_robot_info()
        actions = {
            0 : [0,0,0,0],
            1 : [1,0,1,0],
            2 : [0,1,0,1],
            3 : [0,1,1,0],
            4 : [1,0,0,1],
        }
        for pin, val in zip(self.pinList, actions[res['direction']]):
            GPIO.output(pin, val)
        sleep(res['moving_time'])

class SensingDistance():
    def __init__(self):
        self.sensor = DistanceSensor(27, 17, max_distance=1, threshold_distance=0.1)
        self.led = LED(5)

    def test1(self):
        ro = robot_controller(os.path.dirname(os.path.realpath(__file__)))
        ro.set_robot_info(1)
        self.led.on()
        return redirect(url_for('/stop'))

    def test2(self):
        ro = robot_controller(os.path.dirname(os.path.realpath(__file__)))
        ro.set_robot_info(0)
        self.led.off()

    def run(self):
        self.sensor.when_in_range = self.test1
        self.sensor.when_activated = self.test2

if __name__ == '__main__':
    control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
    move_body = MoveBody(control.get_config()['Robot'])
    s = SensingDistance()
    s.run()
    while True:
        if control.get_robot_info()['status'] == 0:
            move_body.run(1, 0.1)
        else:
            move_body.run(0, 0.1)
    
      