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
    def __init__(self, robot):
        self.robot = robot
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.pinList = self.robot.get_config()['Robot']
        GPIO.setup(self.pinList, GPIO.OUT)

    def run(self, direction, tm):
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

class SensingDistance:
    def __init__(self, robot):
        self.robot = robot
        self.sensor_info = self.robot.get_config()['distance_sensor']
        self.echo = self.sensor_info['echo']
        self.trigger = self.sensor_info['trigger']
        self.signal_led = self.sensor_info['signal_led']
        self.range_distance = self.sensor_info['range_distance']
        self.MAX_DISTANCE = self.sensor_info['max_distance'] 
        self.ROBOT_STATUS_ONE = 1
        self.ROBOT_STATUS_ZERO = 0
        self.led = LED(self.signal_led)
        self.sensor = DistanceSensor(
            echo=self.echo, 
            trigger=self.trigger,
            max_distance= self.MAX_DISTANCE, 
            threshold_distance=self.range_distance
            )
    def change_robot_status_one(self):
        self.robot.set_robot_status(self.ROBOT_STATUS_ONE)
        self.led.on()

    def change_robot_status_zero(self):
        self.robot.set_robot_status(self.ROBOT_STATUS_ZERO)
        self.led.off()

    def run(self):
        self.sensor.when_in_range = self.change_robot_status_one
        self.sensor.when_out_of_range = self.change_robot_status_zero

if __name__ == '__main__':
    robot = robot_controller(os.path.dirname(os.path.realpath(__file__)))
    move_body = MoveBody(robot)
    s = SensingDistance(robot)
    s.run()
    while True:
        if robot.get_robot_info()['status'] == 0:
            move_body.run(1, 1)
        else:
            move_body.run(0, 1)
