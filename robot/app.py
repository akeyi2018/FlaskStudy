# -*- encoding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller import robot_controller, MoveBody, SensingDistance
import os
import json
from time import sleep

app = Flask(__name__)

control = robot_controller(os.path.dirname(os.path.realpath(__file__)))
config = control.get_config()['settings']
control.set_robot_status(config['STATUS_ZERO'])
move_body = MoveBody(control)
sensor = SensingDistance(control)
sensor.run()

def rapper(move_direction):
    control.set_robot_status(config['STATUS_ZERO'])
    while True:
        if control.get_robot_info()['status'] == 0:
            move_body.run(move_direction, config['moving_time'])
        else:
            move_body.run(config['STOP_ROBOT'], config['stop_time'])
            break

@app.route('/', methods=['GET'])
def index():
    return render_template('remote_contol.html')

@app.route('/stop', methods=['POST'])
def stop():
    control.set_robot_status(config['STATUS_ONE'])
    return '200'

@app.route('/move', methods=['POST'])
def move():
    control.set_robot_status(config['STATUS_ONE'])
    if len(request.json) > 0 :
        rapper(int(request.json['d']))
        return '200'
    else:
        return '400' 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)